import os, sys
import time

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:   
    sys.exit("please declare environment variable 'SUMO_HOME'")
    
import traci
import traci.constants

    
sumoCmd = ["sumo-gui", "-c", "roundabout.sumocfg", "--start"]
traci.start(sumoCmd)

print("Starting SUMO")
traci.gui.setSchema("View #0", "real world")


# Add vehicle with id, route and type
# traci.vehicle.add("4", "route2", "type1")


# Dictionary with all the vehicles information
vehicle_information = {}

j = 0
while(j<83):
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
        
        
    j = j+1
traci.close()

for x in vehicle_information:
    vehicle_average_speed = 0
    for y in range(1,len(vehicle_information[x])):
        vehicle_average_speed += vehicle_information[x][y]
    vehicle_average_speed = vehicle_average_speed / (len(vehicle_information[x]) - 1)
    print("Vehicle", x, "  Speed: ", vehicle_average_speed, " Distance: ", vehicle_information[x][0], "time: ", vehicle_information[x][0]/vehicle_average_speed)
    

    
#get network parameters
# IDsOfEdges=traci.edge.getIDList();
# print("IDs of the edges:", IDsOfEdges)
# IDsOfJunctions=traci.junction.getIDList();
# print("IDs of junctions:", IDsOfJunctions)
