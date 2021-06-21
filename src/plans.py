
import os
import json
from traci.main import start
from sys import platform
import csv

from utils import *

# From last episode, create another file with the modifications
# If is the first create a new one with cars and values u want (utils has examples for now)
def update_beliefs(episode, trips, list, route_times={}):
    
    if episode == 1:
        # Create file from utils examples
        # Create "Episodes" folder if dont exists
        if not os.path.exists("Episodes"):
            os.makedirs("Episodes")
        if not os.path.exists("CarCSV"):
            os.makedirs("CarCSV")
        for x in range(1,20):
            carFile = open('CarCSV/'+"car_" + str(x) + '.csv', 'a')

        f = open("Episodes/episode" + str(episode) + ".asl", "w")
        f.write(intial_text) 
        # Add car's beliefs
        f.write(car_test_1)
        f.write(car_test_2)
        f.write(car_test_3)
        f.write(car_test_4)
        f.write(car_test_5)
        f.write(car_test_6)
        f.write(car_test_7)
        f.write(car_test_8)
        f.write(car_test_9)
        f.write(car_test_10)
        f.write(car_test_11)
        f.write(car_test_12)
        f.write(car_test_13)
        f.write(car_test_14)
        f.write(car_test_15)
        f.write(car_test_16)
        f.write(car_test_17)
        f.write(car_test_18)
        f.write(car_test_19)
        f.write(car_test_20)
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
            delay = list[carID][1] #time that the car is waiting to departure
            average_speed = 0
            for y in range(2,len(list[carID])):
                average_speed += list[carID][y]
            average_speed = average_speed / (len(list[carID]) - 2)
            # new_travel_time = list[carID][0]/average_speed
            new_travel_time = list[carID][0]/average_speed + delay
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
            # average = ( float(old_travel_time) * (episode-2) + new_travel_time)/(episode-1) 
            if (float(old_travel_time) == float(0)):
                if(route_times == {}):
                    average = new_travel_time
                else:#ATIS
                    average = 0.4 * (new_travel_time) + 0.6 * (route_times[route_name])
                    print('bdi: ', new_travel_time, 'atis: ', average)
            else:
                if(route_times == {}):
                    average = (0.6*(float(old_travel_time)) + 0.4*new_travel_time)
                else:#ATIS
                    average = 0.4 * ((0.6*float(old_travel_time) + 0.4*new_travel_time)) + 0.6 * (route_times[route_name])
                    print('bdi: ', ((float(old_travel_time) + new_travel_time)/ 2), 'atis: ', average)

            carFile = open('CarCSV/'+"car_" + str(carID) + '.csv', 'a', newline='')
            writer = csv.writer(carFile)
                                                           
            carCSV = [ 
                        carID,
                        trips[int(carID)-1]["arrivalTime"], # Desirable Arrivel Time      
                        trips[int(carID)-1]["departureTime"], #Theoretical Departure Time 
                        route_name, # Route
                        average,# Avg.Route Time        
                        average_speed, #Avg.Speed
                        list[carID][0], #Distance 	
                        new_travel_time, #Travel Time 
                        delay, #Departure Delay 
                        delay + new_travel_time + float(trips[int(carID)-1]["departureTime"]),  #Arrival Time    
                        float(trips[int(carID)-1]["arrivalTime"]) - (delay + new_travel_time +  float(trips[int(carID)-1]["departureTime"])) #Arrival delay
                    ]     

            writer.writerow(carCSV)
            carFile.close()

            data = data.replace(aux_str + old_travel_time +").", aux_str + str(average) +").")
                 
        # Set new day
        data = data.replace("today(" + str(episode-2), "today(" + str(episode-1))
        
        f.write(data)
        f.close()
    

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
