// purpose(Day, Reason).
purpose(4, work).
purpose(5, shopping).
purpose(6, doctor).

// time_of_arrival(Reason, Time).
time_of_arrival(work,0830).

// today(Day).
today(4).

// timeNow(Time).
timeNow(0800).

// route(route_id, time)
route(1,30).
route(2,45).
route(3,40).


get_route(TimeDeparture,Route) :-
    today(Day),
    purpose(Day,Reason),
    time_of_arrival(Reason,TimeArrival),
    route(Route,TravelTime),
    timeNow(TimeNow),
    TimeDeparture is TimeNow + TravelTime.






    





