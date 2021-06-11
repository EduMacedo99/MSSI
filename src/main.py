import os, sys
import traci
import traci.constants

from plans import create_trips, update_beliefs

# Start SUMO
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:   
    sys.exit("please declare environment variable 'SUMO_HOME'")
sumoCmd = ["sumo-gui", "-c", "SUMO/roundabout.sumocfg", "--start"]

#Colors of cars
colors = {"type1":(255,0,0) ,"type2": (255,255,0), "type3": (255,255,255) }

# Dictionary with all the vehicles information
vehicle_information = {}
# vehicle_informations = {"time":0, "distance":0, "speed":[]}
routes_information = {}
trips = []
    
max_episodes = 20
episode = 1


while episode <= max_episodes:
    traci.start(sumoCmd)
    print("Starting SUMO...")
    traci.gui.setSchema("View #0", "real world")
    edges = traci.edge.getIDList()
    # Start episode 
    print("\nEpisode " + str(episode))
    
    steps = 0

    # Update beliefs if any
    update_beliefs(episode, trips, vehicle_information)   
    # Reset vehicle information
    vehicle_information = {}
    # Reset routes information
    routes_information
    
    # Get trips
    # trips is a list with dictionaries [{'carID': _, 'routeName':  _}, ... ]
    print("Getting trips...")
    trips = create_trips(episode)

    # Add trip of each car
    for trip in trips:
        # Teste 1
        traci.vehicle.add(trip["carID"], trip["routeName"], trip["type"], float(trip["departureTime"]))
        traci.vehicle.setColor(trip["carID"], colors[trip["type"]])
        # Teste 1 com um carro diferente
        # if (trip["carID"] == "1"):
        #     traci.vehicle.add(trip["carID"], trip["routeName"], "type2", float(trip["departureTime"]))
        #     traci.vehicle.setColor(trip["carID"],(255,0,0))
        # else:
        #     traci.vehicle.add(trip["carID"], trip["routeName"], "type1", float(trip["departureTime"]))
        #     traci.vehicle.setColor(trip["carID"],(255,255,0))
    
    
    
    while traci.simulation.getMinExpectedNumber() > 0:
        #this runs one simulation step
        # time.sleep(0.5);
        traci.simulationStep()
        steps += 1

        # For each simulation step store
        time = str(traci.simulation.getTime())
        for edge in edges:
            print(traci.edge.getLastStepVehicleNumber(edge))
        # try:
        #     routes_information[time]
        # except:
        #     routes_information[time] = [ [] for _ in range(len(edges)-2) ]
            
        # for edge in edges:
        #     if(edge[0] != ":"):
        #         edge_num = int(edge[len(edge)-1])
        #         routes_information[time][edge_num] = (traci.edge.getLastStepVehicleNumber(edge))
                

        vehicles=traci.vehicle.getIDList()
        for i in range(0,len(vehicles)): 
            # check if car is in dictionary
            try:
                vehicle_information[vehicles[i]]
            except:
            # if car is not in dictionary add it with no values
                vehicle_information[vehicles[i]] = []
                # vehicle_information[vehicles[i]] = {"time":-1, "distance":-1, "speed":[]}
                
            # Update the vehicles information
            if (len(vehicle_information[vehicles[i]]) == 0):
                vehicle_information[vehicles[i]].append(traci.vehicle.getDistance(vehicles[i]))
                vehicle_information[vehicles[i]].append(steps - float(trips[int(vehicles[i])-1]["departureTime"]))
            vehicle_information[vehicles[i]][0] = traci.vehicle.getDistance(vehicles[i])
            vehicle_information[vehicles[i]].append(traci.vehicle.getSpeed(vehicles[i]))
          
        # edges = traci.edge.getIDList()
        # for edge in edges:
        #     print("Number of cars in edge ", edge, ": " ,traci.edge.getLastStepVehicleNumber(edge))


    for x in vehicle_information:
        vehicle_average_speed = 0
        for y in range(2,len(vehicle_information[x])):
            vehicle_average_speed += vehicle_information[x][y]
        vehicle_average_speed = vehicle_average_speed / (len(vehicle_information[x]) - 2)
        print("Vehicle", x, "  Speed: ", round(vehicle_average_speed,3), " Distance: ", round(vehicle_information[x][0],3), "Time: ", round(vehicle_information[x][0]/vehicle_average_speed,3), "Departure Time: ", round(vehicle_information[x][1],3))
    

    episode = episode + 1

    
    traci.close()


