intial_text = """// Day e AverageTravelTime DEVE SER ATUALIZADO A CADA EPISODIO 
"""

car_test_1 = """
today(0, 1).
route("route0", 1, 0).
route("route1", 1, 0).
route("route2", 1, 0).
desirable_arrival_time(1, 0830).
usual_departure_time(1, 0800).
expected_travel_time(1, 999).
"""

car_test_2 = """
today(0, 2).
route("route0", 2, 0).
route("route1", 2, 0).
route("route2", 2, 0).
desirable_arrival_time(2, 0830).
usual_departure_time(2, 0800).
expected_travel_time(2, 999).
"""

car_test_3 = """
today(0, 3).
route("route0", 3, 0).
route("route1", 3, 0).
route("route2", 3, 0).
desirable_arrival_time(3, 0830).
usual_departure_time(3, 0800).
expected_travel_time(3, 999).
"""

car_test_4 = """
today(0, 4).
route("route0", 4, 0).
route("route1", 4, 0).
route("route2", 4, 0).
desirable_arrival_time(4, 0830).
usual_departure_time(4, 0800).
expected_travel_time(4, 999).
"""

car_test_5 = """
today(0, 5).
route("route0", 5, 0).
route("route1", 5, 0).
route("route2", 5, 0).
desirable_arrival_time(5, 0830).
usual_departure_time(5, 0800).
expected_travel_time(5, 999).
"""

plans = """
// NAO E PRECISO MEXER EM PRINCIPIO
time_now(0800).

+today(Day, CarID) : true
    <- ? desirable_arrival_time(CarID, DesirableArrivalTime);
       ! bestRoute(CarID);
       ? expected_travel_time(CarID, ExpectedT);
       ? route(R, CarID, ExpectedT);
       .print("{'carID': '", CarID, "','routeName': '", R, "'}").

+!bestRoute(CarID) : route(R, CarID, T) &  expected_travel_time(CarID, ExpectedT) & (T < ExpectedT)
    <- - expected_travel_time(CarID, ExpectedT);
       + expected_travel_time(CarID, T);
       ! bestRoute(CarID).
       
+!bestRoute(CarID) : true <- true.
"""