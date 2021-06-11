////////////////
//  Beliefs   //
////////////////

// today(Day, CarID).
today(0, 1).
today(0, 2).

// time_now(Time).
time_now(0800).

// route(RouteName, CarID, AverageTravelTime).
route("route0", 1, 60).
route("route1", 1, 30).//<- car 1 deve escolher a rota 1
route("route2", 1, 50).
route("route0", 2, 70).
route("route1", 2, 80).
route("route2", 2, 50).//<- car 2 deve escolher a rota 2

// car_type(CarID, DesirableArrivalTime).
car_type(1, "type1").
car_type(2, "type2").

// desirable_arrival_time(CarID, DesirableArrivalTime).
desirable_arrival_time(1, 0090).
desirable_arrival_time(2, 0100).


// expected_travel_time(CarID, ExpectTime).
expected_travel_time(1, 999).//valor pessimista
expected_travel_time(2, 999).

//////////////
//  Plans   //
//////////////

+today(Day, CarID) : true
    <- ? desirable_arrival_time(CarID, DesirableArrivalTime);// Get desirable arrival time to use later
       ! bestRoute(CarID);// Set the best expected travel time 
       ? expected_travel_time(CarID, ExpectedT);// Get best expected travel time 
       ? route(R, CarID, ExpectedT);// Get route that has that travel time as average
       !chooseDepartureTime(R,CarID). // Set the departure time
       
// Escolhe uma rota random
+!anyRoute : route(RouteName, CarID, AverageTravelTime)
    <- .print("Route: ", RouteName).

// Coloca no belief expected_travel_time o menor valor possivel
+!bestRoute(CarID) : route(R, CarID, T) &  expected_travel_time(CarID, ExpectedT) & (T < ExpectedT)
    <- //.print(R, "tem average time de", T, ", menor que o expectavel", ExpectedT);
       + tripRoute(R,CarID);
       - expected_travel_time(CarID, ExpectedT);
       + expected_travel_time(CarID, T);
       ! bestRoute(CarID).
// Quando o de cima nao for verdade (ou seja, nao sobra nenhuma rota que satisfaca aquilo)
+!bestRoute(CarID) : true <- true.

// Escolhe o departure time
+!chooseDepartureTime(R,CarID) : tripRoute(R,CarID)
    <- ?today(Day, CarID);
       ?desirable_arrival_time(CarID, DesirableArrivalTime);
       ?route(R, CarID, AverageTravelTime);
       +tripDepartureTime(DesirableArrivalTime - AverageTravelTime, R);
       ?car_type(CarID, TypeName);
       .print("{'carID': '", CarID, "','routeName': '",R, "','type': '", TypeName, "', 'departureTime': '", DesirableArrivalTime - AverageTravelTime, "'}").









    





