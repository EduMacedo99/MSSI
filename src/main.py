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
traci.start(sumoCmd)
print("Starting SUMO...")
traci.gui.setSchema("View #0", "real world")


# Dictionary with all the vehicles information
vehicle_information = {}
trips = []
    
max_episodes = 3
episode = 1


while episode <= max_episodes:
    # Start episode 
    print("\nEpisode " + str(episode))
    
    # Update beliefs if any
    update_beliefs(episode, trips, vehicle_information)   
    vehicle_information = {}
    
    # Get trips
    # trips is a list with dictionaries [{'carID': _, 'routeName':  _}, ... ]
    print("Getting trips...")
    trips = create_trips(episode);

    # Add trip of each car
    for trip in trips:
        # traci.vehicle.add(id, route, type, departure_time)
        traci.vehicle.add(trip["carID"], trip["routeName"], "type1", 0)#TODO: Atualizar departure time
    

    while traci.simulation.getMinExpectedNumber() > 0:
        #this runs one simulation step
        # time.sleep(0.5);
        traci.simulationStep()
        
        vehicles=traci.vehicle.getIDList()
        for i in range(0,len(vehicles)): 
            # check if car is in dictionary
            try:
                vehicle_information[vehicles[i]]
            except:
            # if car is not in dictionary add it with no values
                print("HERE ONLY ONCE PER CAR")
                vehicle_information[vehicles[i]] = []
                
            # Update the vehicles information
            if (len(vehicle_information[vehicles[i]]) == 0):
                vehicle_information[vehicles[i]].append(traci.vehicle.getDistance(vehicles[i]))
            vehicle_information[vehicles[i]][0] = traci.vehicle.getDistance(vehicles[i])
            vehicle_information[vehicles[i]].append(traci.vehicle.getSpeed(vehicles[i]))


    for x in vehicle_information:
        vehicle_average_speed = 0
        for y in range(1,len(vehicle_information[x])):
            vehicle_average_speed += vehicle_information[x][y]
        vehicle_average_speed = vehicle_average_speed / (len(vehicle_information[x]) - 1)
        print("Vehicle", x, "  Speed: ", vehicle_average_speed, " Distance: ", vehicle_information[x][0], "time: ", vehicle_information[x][0]/vehicle_average_speed)
        
    # Next episode
    episode = episode + 1
    #if episode <= max_episodes: 
    #    input("next?")
    
traci.close()
    
#get network parameters
# IDsOfEdges=traci.edge.getIDList();
# print("IDs of the edges:", IDsOfEdges)
# IDsOfJunctions=traci.junction.getIDList();
# print("IDs of junctions:", IDsOfJunctions)
