intial_text = """// Day e AverageTravelTime DEVE SER ATUALIZADO A CADA EPISODIO 
"""
# Test 1 and 3
car_test_1 = """
today(0, 1).
route("route0", 1, 0).
route("route1", 1, 0).
route("route2", 1, 0).
desirable_arrival_time(1, 090).
expected_travel_time(1, 999).
car_type(1, "type1").
"""

car_test_2 = """
today(0, 2).
route("route0", 2, 0).
route("route1", 2, 0).
route("route2", 2, 0).
desirable_arrival_time(2, 0120).
expected_travel_time(2, 999).
car_type(2, "type1").
"""

car_test_3 = """
today(0, 3).
route("route0", 3, 0).
route("route1", 3, 0).
route("route2", 3, 0).
desirable_arrival_time(3, 0110).
expected_travel_time(3, 999).
car_type(3, "type1").
"""

car_test_4 = """
today(0, 4).
route("route0", 4, 0).
route("route1", 4, 0).
route("route2", 4, 0).
desirable_arrival_time(4, 0125).
expected_travel_time(4, 999).
car_type(4, "type1").
"""

car_test_5 = """
today(0, 5).
route("route0", 5, 0).
route("route1", 5, 0).
route("route2", 5, 0).
desirable_arrival_time(5, 0150).
expected_travel_time(5, 999).
car_type(5, "type1").
"""

# Test 2 and 4
# car_test_1 = """
# today(0, 1).
# route("route0", 1, 0).
# route("route1", 1, 0).
# route("route2", 1, 0).
# desirable_arrival_time(1, 0090).
# expected_travel_time(1, 999).
# car_type(1, "type1").
# """

# car_test_2 = """
# today(0, 2).
# route("route0", 2, 0).
# route("route1", 2, 0).
# route("route2", 2, 0).
# desirable_arrival_time(2, 0100).
# expected_travel_time(2, 999).
# car_type(2, "type2").
# """

# car_test_3 = """
# today(0, 3).
# route("route0", 3, 0).
# route("route1", 3, 0).
# route("route2", 3, 0).
# desirable_arrival_time(3, 0080).
# expected_travel_time(3, 999).
# car_type(3, "type1").
# """

# car_test_4 = """
# today(0, 4).
# route("route0", 4, 0).
# route("route1", 4, 0).
# route("route2", 4, 0).
# desirable_arrival_time(4, 0078).
# expected_travel_time(4, 999).
# car_type(4, "type2").
# """

# car_test_5 = """
# today(0, 5).
# route("route0", 5, 0).
# route("route1", 5, 0).
# route("route2", 5, 0).
# desirable_arrival_time(5, 0120).
# expected_travel_time(5, 999).
# car_type(5, "type3").
# """

plans = """
// NAO E PRECISO MEXER EM PRINCIPIO

+today(Day, CarID) : true
    <- ? desirable_arrival_time(CarID, DesirableArrivalTime);
       ! bestRoute(CarID);
       ? expected_travel_time(CarID, ExpectedT);
       ? route(R, CarID, ExpectedT);
       !chooseDepartureTime(R,CarID).

+!bestRoute(CarID) : route(R, CarID, T) &  expected_travel_time(CarID, ExpectedT) & (T < ExpectedT)
    <- + tripRoute(R,CarID);
       - expected_travel_time(CarID, ExpectedT);
       + expected_travel_time(CarID, T);
       ! bestRoute(CarID).
       
+!bestRoute(CarID) : true <- true.

+!chooseDepartureTime(R,CarID) : tripRoute(R,CarID)
    <- ?today(Day, CarID);
       ?desirable_arrival_time(CarID, DesirableArrivalTime);
       ?route(R, CarID, AverageTravelTime);
       +tripDepartureTime(DesirableArrivalTime - AverageTravelTime, R);
       ?car_type(CarID, TypeName);
       .print("{'carID': '", CarID, "','routeName': '",R, "','type': '", TypeName, "', 'departureTime': '", DesirableArrivalTime - AverageTravelTime, "'}").
"""