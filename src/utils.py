intial_text = """// Day e AverageTravelTime DEVE SER ATUALIZADO A CADA EPISODIO 
"""
# Test 1 and 3


car_test_1 = """
today(0, 1).
route("route0", 1, 0).
route("route1", 1, 0).
route("route2", 1, 0).
desirable_arrival_time(1, 0180).
expected_travel_time(1, 9999).
car_type(1, "type1").
"""

car_test_2 = """
today(0, 2).
route("route0", 2, 0).
route("route1", 2, 0).
route("route2", 2, 0).
desirable_arrival_time(2, 0200).
expected_travel_time(2, 9999).
car_type(2, "type1").
"""

car_test_3 = """
today(0, 3).
route("route0", 3, 0).
route("route1", 3, 0).
route("route2", 3, 0).
desirable_arrival_time(3, 0220).
expected_travel_time(3, 9999).
car_type(3, "type1").
"""

car_test_4 = """
today(0, 4).
route("route0", 4, 0).
route("route1", 4, 0).
route("route2", 4, 0).
desirable_arrival_time(4, 0240).
expected_travel_time(4, 9999).
car_type(4, "type1").
"""

car_test_5 = """
today(0, 5).
route("route0", 5, 0).
route("route1", 5, 0).
route("route2", 5, 0).
desirable_arrival_time(5, 0260).
expected_travel_time(5, 9999).
car_type(5, "type1").
"""

car_test_6 = """
today(0, 6).
route("route0", 6, 0).
route("route1", 6, 0).
route("route2", 6, 0).
desirable_arrival_time(6, 0260).
expected_travel_time(6, 9999).
car_type(6, "type1").
"""

car_test_7 = """
today(0, 7).
route("route0", 7, 0).
route("route1", 7, 0).
route("route2", 7, 0).
desirable_arrival_time(7, 0270).
expected_travel_time(7, 9999).
car_type(7, "type1").
"""

car_test_8 = """
today(0, 8).
route("route0", 8, 0).
route("route1", 8, 0).
route("route2", 8, 0).
desirable_arrival_time(8, 0210).
expected_travel_time(8, 9999).
car_type(8, "type1").
"""

car_test_9 = """
today(0, 9).
route("route0", 9, 0).
route("route1", 9, 0).
route("route2", 9, 0).
desirable_arrival_time(9, 0190).
expected_travel_time(9, 9999).
car_type(9, "type1").
"""

car_test_10 = """
today(0, 10).
route("route0", 10, 0).
route("route1", 10, 0).
route("route2", 10, 0).
desirable_arrival_time(10, 0165).
expected_travel_time(10, 9999).
car_type(10, "type1").
"""

car_test_11 = """
today(0, 11).
route("route0", 11, 0).
route("route1", 11, 0).
route("route2", 11, 0).
desirable_arrival_time(11, 0170).
expected_travel_time(11, 9999).
car_type(11, "type1").
"""

car_test_12 = """
today(0, 12).
route("route0", 12, 0).
route("route1", 12, 0).
route("route2", 12, 0).
desirable_arrival_time(12, 0200).
expected_travel_time(12, 9999).
car_type(12, "type1").
"""

car_test_13 = """
today(0, 13).
route("route0", 13, 0).
route("route1", 13, 0).
route("route2", 13, 0).
desirable_arrival_time(13, 0195).
expected_travel_time(13, 9999).
car_type(13, "type1").
"""

car_test_14 = """
today(0, 14).
route("route0", 14, 0).
route("route1", 14, 0).
route("route2", 14, 0).
desirable_arrival_time(14, 0280).
expected_travel_time(14, 9999).
car_type(14, "type1").
"""

car_test_15 = """
today(0, 15).
route("route0", 15, 0).
route("route1", 15, 0).
route("route2", 15, 0).
desirable_arrival_time(15, 0300).
expected_travel_time(15, 9999).
car_type(15, "type1").
"""

car_test_16 = """
today(0, 16).
route("route0", 16, 0).
route("route1", 16, 0).
route("route2", 16, 0).
desirable_arrival_time(16, 0315).
expected_travel_time(16, 9999).
car_type(16, "type1").
"""

car_test_17 = """
today(0, 17).
route("route0", 17, 0).
route("route1", 17, 0).
route("route2", 17, 0).
desirable_arrival_time(17, 0185).
expected_travel_time(17, 9999).
car_type(17, "type1").
"""

car_test_18 = """
today(0, 18).
route("route0", 18, 0).
route("route1", 18, 0).
route("route2", 18, 0).
desirable_arrival_time(18, 0190).
expected_travel_time(18, 9999).
car_type(18, "type1").
"""

car_test_19 = """
today(0, 19).
route("route0", 19, 0).
route("route1", 19, 0).
route("route2", 19, 0).
desirable_arrival_time(19, 0195).
expected_travel_time(19, 9999).
car_type(19, "type1").
"""

car_test_20 = """
today(0, 20).
route("route0", 20, 0).
route("route1", 20, 0).
route("route2", 20, 0).
desirable_arrival_time(20, 0150).
expected_travel_time(20, 9999).
car_type(20, "type1").
"""



'''
# Test 2 and 4
car_test_1 = """
today(0, 1).
route("route0", 1, 0).
route("route1", 1, 0).
route("route2", 1, 0).
desirable_arrival_time(1, 0090).
expected_travel_time(1, 9999).
car_type(1, "type1").
"""

car_test_2 = """
today(0, 2).
route("route0", 2, 0).
route("route1", 2, 0).
route("route2", 2, 0).
desirable_arrival_time(2, 0120).
expected_travel_time(2, 9999).
car_type(2, "type2").
"""

car_test_3 = """
today(0, 3).
route("route0", 3, 0).
route("route1", 3, 0).
route("route2", 3, 0).
desirable_arrival_time(3, 0110).
expected_travel_time(3, 9999).
car_type(3, "type1").
"""

car_test_4 = """
today(0, 4).
route("route0", 4, 0).
route("route1", 4, 0).
route("route2", 4, 0).
desirable_arrival_time(4, 0125).
expected_travel_time(4, 9999).
car_type(4, "type2").
"""

car_test_5 = """
today(0, 5).
route("route0", 5, 0).
route("route1", 5, 0).
route("route2", 5, 0).
desirable_arrival_time(5, 0150).
expected_travel_time(5, 9999).
car_type(5, "type3").
"""

'''

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
       .print("{'carID': '", CarID, "','routeName': '",R, "','type': '", TypeName, "', 'departureTime': '", DesirableArrivalTime - AverageTravelTime, "','arrivalTime': '",DesirableArrivalTime, "'}").
"""