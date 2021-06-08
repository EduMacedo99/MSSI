// Day e AverageTravelTime DEVE SER ATUALIZADO A CADA EPISODIO 

today(1, 1).
route("route0", 1, 0).
route("route1", 1, 60.00000000000001).
route("route2", 1, 0).
desirable_arrival_time(1, 0090).
expected_travel_time(1, 999).

today(1, 2).
route("route0", 2, 75.00000000000001).
route("route1", 2, 0).
route("route2", 2, 0).
desirable_arrival_time(2, 0100).
expected_travel_time(2, 999).

today(1, 3).
route("route0", 3, 76.00000000000003).
route("route1", 3, 0).
route("route2", 3, 0).
desirable_arrival_time(3, 0080).
expected_travel_time(3, 999).

today(1, 4).
route("route0", 4, 74.00000000000001).
route("route1", 4, 0).
route("route2", 4, 0).
desirable_arrival_time(4, 0078).
expected_travel_time(4, 999).

today(1, 5).
route("route0", 5, 76.00000000000001).
route("route1", 5, 0).
route("route2", 5, 0).
desirable_arrival_time(5, 0120).
expected_travel_time(5, 999).

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
       .print("{'carID': '", CarID, "','routeName': '", R, "', 'departureTime': '", DesirableArrivalTime - AverageTravelTime, "'}").
