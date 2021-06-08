### MSSI

# AgentSpeak(ficheiro) <-> Traci <-> SUMO

1- criar ficheiro .asl com os beliefs e goals/desires iniciais
2- correr o comando que executa o ficheiro e analisar o output que vai ser do tipo: (agent_id, route_id, departure_time?), ...
3- add cars com os parametros de cima, com o Traci no SUMO
4- analisar output dos tempos
5- atualizar os beliefs no ficheiro .asl
6- repetir 2


TODO: 
* Como se faz o while de episodios (terminar o sumo e voltar a abrir?)
* como adicionar os carros, ler ficheiro' ou random
* adicionar o tipo de carro MAX SPEED aos beliefs

# Scenario 1:
In the first scenario, we assume that the drivers can not ask for help. Hence their decision-making process to choose the route is solely done by their own set of base beliefs.

# Scenario 2:
A traveler information system (ATIS) agent will be added to the system as a second scenario. Thus each driver at the beginning of the run can ask for advice (occupation, travel time, average speed, etc.), thereby based on the ATIS response and in their set of beliefs, they will choose the most suitable route.
- get velocidade e distancia de cada edge do sumo ou guardar no main.py
- atualizar o belief do average time com esses valores 60% ATIS_TIME + 40% CAR_BELIEF_SCENARIO_1

# Scenario 3:
As a final scenario, it would be interesting to study the network by reversing the roles, which means, the BDI agent would be the ATIS instead of the drivers. Therefore the population of drivers would ask for help to choose the route in the beginning of the run, and our ATIS agent based on it is set of beliefs would answer with the route that is appropriate for each driver.
- route(routeName, capacidade, average_time)