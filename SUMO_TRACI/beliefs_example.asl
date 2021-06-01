#########Igual para todos os agentes
adjacent(gneJ0,gneE1).
adjacent(gneE2,gneJ1).
adjacent(gneJ0,gneJ1).
adjacent(gneJ0,gneE3).
adjacent(gneE4,gneJ1).

route(gneJ0, gneJ1, 40, [gneE1,gneE2]).
route(gneJ0, gneJ1, 30, [gneE0]).
route(gneJ0, gneJ1, 50, [gneE3,gneE4]).

purpose(4, work).
purpose(5, shopping).
purpose(6, doctor).


########Podemos mudar o purpose
destination(work, gneJ1)


########Mudar o purpose em perceivedArrivalCost
perceivedArrivalCost(10, work).
usualDepartureTime(gneJ0,gneJ1, 0815).
expectedTravelTime(gneJ0,gneJ1, 999).

########Mudar a Route que o Driver começa
tripRoute(gneJ0, gneJ1, 40, [gneE1,gneE2]).
tripDepartureTime(0815, [gneE1,gneE2]).

today(4).

timeNow(0800).
