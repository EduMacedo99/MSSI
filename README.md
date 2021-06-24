### MSSI

# How to run
Go to src folder and run the following command:

```python3 main.py Num_Random_Cars [0-1000] Agent [BDI ... ATIS] Accident [True - False]```

or

```python main.py Num_Random_Cars [0-1000] Agent [BDI ... ATIS] Accident [True - False]```

# Scenario 1:
In the first scenario, we assume that the drivers can not ask for help. Hence their decision-making process to choose the route is solely based on their own set of base beliefs.

# Scenario 2:
A traveler information system (ATIS) agent will be added to the system as a second scenario. Thus each driver at the beginning of the run can ask for advice (travel time, average speed, etc.), thereby based on the ATIS response and on their set of beliefs, they will choose the most suitable route.


# Scenario 3:
For the third scenario, we assume that the drivers can not ask for help. Hence their decision-making process to choose the route is solely based on their own set of base beliefs. From episode 50 onward there is a simmulated accident in the network, which reduces the number of lanes in one of the routes.

# Scenario 4:
A traveler information system (ATIS) agent will be added to the system as a second scenario. Thus each driver at the beginning of the run can ask for advice (travel time, average speed, etc.), thereby based on the ATIS response and on their set of beliefs, they will choose the most suitable route. From episode 50 onward there is a simmulated accident in the network, which reduces the number of lanes in one of the routes.
