// Beliefs

//routes(Route_ID,travel_time)
route(1,999).
route(2,999).
route(3,999).

// today(Day).
today(4).
today(5).

// time_now(Time).
time_now(0800).

// time_of_arrival(Day, Des_Arri_Time)
desirable_arrival_time(4, 0830).
desirable_arrival_time(5, 0830).

+today(Day) : true
    <- ? desirable_arrival_time(Day, Des_Arri_Time);
       ! anyRoute(Route_ID).

+!anyRoute(Route_ID): route(Route_ID,Travel_Time)
    <- .print("El carro es ",Route_ID).


//+!get_route(Route_ID) : route(id,travel_time)
//    <-  ?today(Day);
//        ?time_of_arrival(Day,TimeArrival);
//       !route(Route,TravelTime).









    





