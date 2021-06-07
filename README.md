### MSSI

# AgentSpeak(ficheiro) <-> Traci <-> SUMO

1- criar ficheiro .asl com os beliefs e goals/desires iniciais
2- correr o comando que executa o ficheiro e analisar o output que vai ser do tipo: (agent_id, route_id, departure_time?), ...
3- add cars com os parametros de cima, com o Traci no SUMO
4- analisar output dos tempos
5- atualizar os beliefs no ficheiro .asl
6- repetir 2


TODO: 
Atualizar o dia
Como se faz o while de episodios (terminar o sumo e voltar a abrir?)
dar Departure time no add cars
usar DesirableArrivalTime nos plans
como adicionar os carros, ler ficheiro 

mais cenarios :|