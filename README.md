# Conflict_Dynamics
Mod of davidcairuz/ecosystem-simulation

The system presented consists of a flat 500x500 terrain, and two opposing sides (blue and
red), each one of wich has in his territory, a place where new individuals from are produced every time
some member consumes resources. The territories are separated by a barrier with a gate of variable position and size.
 Each agent is capable of consuming a resource (green dots) and to choose whether to eliminate or not
an opponent agent, each time there is a meeting. Each event in which a member of a side encounters a member of the opposing side is registered as Tension, and each time one agent kills another it is registered as Assassination. Every agent has a basal mean life, given by the maximum time it can remain without consuming any resources. The cooperative characteristic of the colony is in the reproductive path: the colony benefits from one of its members consuming a resource because this way its population increases, which makes more likely that more resources will be consumed and that the colony will survive longer. The simulation ends when it meets one of the following conditions: (1) the number of resources is equal to 0, or (b) the total number of individuals is
equal to 0. Resources can be chosen as non-renewable (the maximum number of resources is the initial one), or as renewable (new resources appear with a certain tf rate).
In the last case, fluctuations in the population number may occur, imposing the need to stop the simulation manually.

For calling the program run ``` python simulation.py ```

![image](https://github.com/ManuLado/Conflict_Dynamics/blob/8040b55033754a145e77218a2c7210f783b7e7e0/Screenshot%202021-12-24%20141731.png)
