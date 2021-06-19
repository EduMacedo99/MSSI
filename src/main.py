import os, sys
import traci
import traci.constants
import random

from plans import create_trips, update_beliefs

def print_vehicle_information(vehicle_information):
    for x in vehicle_information:
        vehicle_average_speed = 0
        for y in range(2,len(vehicle_information[x])):
            vehicle_average_speed += vehicle_information[x][y]
        vehicle_average_speed = vehicle_average_speed / (len(vehicle_information[x]) - 2)
        print("Vehicle", x, "  Speed: ", round(vehicle_average_speed,3), " Distance: ", round(vehicle_information[x][0],3), "TravelTime_SUMO: ", round(vehicle_information[x][0]/vehicle_average_speed,3), "Delay: ", round(vehicle_information[x][1],3))
    
def add_random_vehicles(traci, cars_num):
    for x in range(0,int(cars_num/10)):
        for y  in range(0,10):
            traci.vehicle.add("random"+str((10*x+y)), "route"+str(random.randint(0,2)), "type"+str(random.randint(1,3)), 50 + (5 * x))
            traci.vehicle.setColor("random"+str((10*x+y)), (255,20,147))

def atis_update_information(trips,vehicle_information):
    route_times = {}
    for trip in trips:
        vehicle_average_speed = 0
        for x in range(2,len(vehicle_information[trip["carID"]])):
            vehicle_average_speed += vehicle_information[trip["carID"]][x]
        vehicle_average_speed = vehicle_average_speed / (len(vehicle_information[trip["carID"]]) - 2)
        vehicle_average_time = vehicle_information[trip["carID"]][0] / vehicle_average_speed
        try:
            routes_information[trip["routeName"]]
            route_times[trip["routeName"]]
        except:
            routes_information[trip["routeName"]] = []
            route_times[trip["routeName"]] = 0
        routes_information[trip["routeName"]].append(vehicle_average_time)
    
    # print(routes_information)
    for routes in routes_information:
        route_speed = 0
        for speeds in routes_information[routes]:
            route_speed += speeds
        route_average_speed = route_speed / len(routes_information[routes])
        route_times[routes] = route_average_speed

    return route_times


num_random_cars = 0
atis = False
accident = False

try:
	if(sys.argv[1] and sys.argv[2] and sys.argv[3]):
		print("")
except:
	print("To run please provide the following arguments: Num_Random_Cars [0-1000] Agent [BDI ... ATIS] Accident [True - False]")
	exit()

if( 0 <= int(sys.argv[1]) <= 1000):
    num_random_cars = int(sys.argv[1])
else:
	print("To run please provide the following arguments: Num_Random_Cars [0-1000] Agent [BDI ... ATIS] Accident [True - False]")
	exit()

if(sys.argv[2] == "BDI"):
	atis = False
elif(sys.argv[2] == "ATIS"):
	atis = True
else:
	print("To run please provide the following arguments: Num_Random_Cars [0-1000] Agent [BDI ... ATIS] Accident [True - False]")
	exit()

if(sys.argv[3] == "True"):
	accident = True
elif(sys.argv[3] == "False"):
	accident = False
else:
	print("To run please provide the following arguments: Num_Random_Cars [0-1000] Agent [BDI ... ATIS] Accident [True - False]")
	exit()


# Start SUMO
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:   
    sys.exit("please declare environment variable 'SUMO_HOME'")
sumoCmd = ["sumo-gui", "-c", "SUMO/clear_road.sumocfg", "--start"]

#Colors of cars
colors = {"type1":(0,255,0) ,"type2": (255,255,0), "type3": (255,255,255) }

# Dictionary with all the vehicles information
vehicle_information = {}
# vehicle_informations a list of lists. First index is the vehicle_ID and the second is an index for the following list {"distance":0, "time":0, "speed":[]}
routes_information = {}
route_times = {}
trips = []
    
max_episodes = 100
episode = 1

traci.start(sumoCmd)
print("Starting SUMO...")
traci.gui.setSchema("View #0", "real world")
    
while episode <= max_episodes:

    # Abre 1 janela do Sumo (Clicar start o mesmo numero de episodios)
    if accident:
        if (episode < 15):
            traci.load(['-c', "SUMO/clear_road.sumocfg", "--start"])
        else:
            traci.load(['-c', "SUMO/accident.sumocfg", "--start"])
    else:
            traci.load(['-c', "SUMO/clear_road.sumocfg", "--start"])
    
    edges = traci.edge.getIDList()
    # Start episode 
    print("\nEpisode " + str(episode))
    
    steps = 0

    # Test 3 and 4
    add_random_vehicles(traci, num_random_cars)

    # Update beliefs if any
    update_beliefs(episode, trips, vehicle_information, route_times)   
    # Reset vehicle information
    vehicle_information = {}
    route_times = {}

    # Reset routes information
    routes_information = {}
    
    # Get trips
    # trips is a list with dictionaries [{'carID': _, 'routeName':  _}, ... ]
    print("Getting trips...")
    trips = create_trips(episode)
    i=0
    # Add trip of each car
    for trip in trips:
        # Caso recebemos um valore negativo do departure time passa para 0
        if float(trip["departureTime"]) < 0:
            trips[i]["departureTime"] = "0"

        i += 1
        traci.vehicle.add(trip["carID"], trip["routeName"], trip["type"], float(trip["departureTime"]))
        traci.vehicle.setColor(trip["carID"], colors[trip["type"]])
    
    
    while traci.simulation.getMinExpectedNumber() > 0:
        #this runs one simulation step
        # time.sleep(0.5);
        traci.simulationStep()
        steps += 1

        # For each simulation step store
        time = str(traci.simulation.getTime())

            
        vehicles=traci.vehicle.getIDList()
        for i in range(0,len(vehicles)): 
            # check if car is in dictionary
            # print(vehicles[i])
            if(vehicles[i].find("random") == -1):
                try:
                    vehicle_information[vehicles[i]]
                except:
                # if car is not in dictionary add it with no values
                    vehicle_information[vehicles[i]] = []
                    # vehicle_information[vehicles[i]] = {"distance":-1, "time":-1, "speed":[]}
                    
                # Update the vehicles information
                if (len(vehicle_information[vehicles[i]]) == 0):
                    vehicle_information[vehicles[i]].append(traci.vehicle.getDistance(vehicles[i]))
                    vehicle_information[vehicles[i]].append((steps-1) - float(trips[int(vehicles[i])-1]["departureTime"]))
                # Update speed and distance travelled 
                vehicle_information[vehicles[i]][0] = traci.vehicle.getDistance(vehicles[i])
                vehicle_information[vehicles[i]].append(traci.vehicle.getSpeed(vehicles[i]))
          

    print_vehicle_information(vehicle_information)
    
    if atis:
        route_times = atis_update_information(trips,vehicle_information)
    
        

    episode = episode + 1
    
traci.close(False)
    
        



