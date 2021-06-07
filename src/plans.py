
import os
import json
from traci.main import start
from sys import platform

from utils import intial_text, car_test_1, car_test_2, plans

# From last episode, create another file with the modifications
# If is the first create a new one with cars and values u want (utils has examples for now)
def update_beliefs(episode, trips, list):
    
    if episode == 1:
        # Create file from utils examples
        # Create "Episodes" folder if dont exists
        if not os.path.exists("Episodes"):
            os.makedirs("Episodes")
        f = open("Episodes/episode" + str(episode) + ".asl", "w")
        f.write(intial_text) 
        # Add car's beliefs
        f.write(car_test_1)
        f.write(car_test_2)
        # Add plan
        f.write(plans)
        f.close()
    else:
        # Copy and update last episode
        f_last = open("Episodes/episode" + str(episode-1) + ".asl", "r")
        f = open("Episodes/episode" + str(episode) + ".asl", "w")
        data = f_last.read()
        f_last.close()
        
        # Replace informarion
        for carID in list:
            average_speed = 0
            for y in range(1,len(list[carID])):
                average_speed += list[carID][y]
            average_speed = average_speed / (len(list[carID]) - 1)
            new_travel_time = list[carID][0]/average_speed
            route_name = trips[int(carID)-1]["routeName"]
            
            # Get old travel time 
            # route("route0", 1, 60).
            aux_str = route_name +'", ' + carID +', '
            old_travel_time_index = data.find(aux_str) +len(aux_str)
            i = old_travel_time_index
            old_travel_time = ""
            while data[i] != ")":
                old_travel_time = old_travel_time + data[i]
                i = i + 1
                
            # Set new travel time
            # Calculate new average, dont count default values
            average = ( float(old_travel_time) * (episode-2) + new_travel_time)/(episode-1) 
            data = data.replace(aux_str + old_travel_time +").", aux_str + str(average) +").")
                 
        # Set new day
        # TODO:
        f.write(data)
        f.close()
        
    return 


# Creates asl file for the first episode
# Executes command
# Parse output
# Returns a list with dictionaries of each car
def create_trips(episode):
    ## Executes command
    if platform == "linux" or platform == "linux2":
        stream = os.popen("python3 -m agentspeak Episodes/episode" + str(episode) + ".asl")
    else:
        stream = os.popen("python -m agentspeak Episodes/episode" + str(episode) + ".asl")
    output = stream.read()
    print(output)
    
    ## Parse output
    # clean output
    output = output.replace("episode" + str(episode) + " ","")
    output = output.replace("'",'"')
    output = output.replace(" ","")
    trips = output.split("\n")
    # create a list with cars information
    res = []
    for trip in trips:
        if trip:
            # convert car dictionary string to an actually dictionary
            res.append(json.loads(trip))

    # res = [{'carID': _, 'routeName':  _}, ... ]
    return res
