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

// desirable_arrival_time(CarID, DesirableArrivalTime).
desirable_arrival_time(1, 0830).
desirable_arrival_time(2, 0830).

// usual_departure_time(CarID, UsualDepartureTime).
usual_departure_time(1, 0800).//valor minimo?
usual_departure_time(2, 0800).

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
       .print("{'carID': '", CarID, "','routeName': '", R, "'}").
       
// Escolhe uma rota random
+!anyRoute : route(RouteName, CarID, AverageTravelTime)
    <- .print("Route: ", RouteName).

// Coloca no belief expected_travel_time o menor valor possivel
+!bestRoute(CarID) : route(R, CarID, T) &  expected_travel_time(CarID, ExpectedT) & (T < ExpectedT)
    <- //.print(R, "tem average time de", T, ", menor que o expectavel", ExpectedT);
       - expected_travel_time(CarID, ExpectedT);// Em todos os exemplos n é preciso remover mas so da assim ノಠ_ಠノ
       + expected_travel_time(CarID, T);
       ! bestRoute(CarID).
// Quando o de cima nao for verdade (ou seja, nao sobra nenhuma rota que satisfaca aquilo)
+!bestRoute(CarID) : true <- true.


// TODO:Escolhe o departure time
//+!chooseDepartureTime(DesirableArrivalTime) :







    





