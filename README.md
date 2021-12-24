# Conflict_Dynamics
Mod of davidcairuz/ecosystem-simulation

The system presented consists of a flat 500x500 terrain, and two opposing sides (blue and
red), which each one has in his territory, a place where new individuals from his own side are produced each time
that some member consumes resources. The territories are separated by a barrier with a gate for position and size.
variable years. Each agent is capable of consuming a resource (green dots) and to choose whether to eliminate or not
to an agent of the opposite side, each time there is a meeting. Each event in which a member of a side encounters a member of the opposing side, registers as Tension, and each time one agent kills another it is recorded as Assassination. Every agent has a hope of
base life, given by the maximum time that can remain without consuming any resources. The cooperative characteristic of the colony is in the reproductive path: the colony is benefits from one of its members consuming a resource because in this way its population increases, which makes more likely that more resources will be consumed and that the colony will survive longer. The simulation ends when
meets one of the following conditions: (1) the number of resources is equal to 0, or (b) the total number of individuals is
equal to 0. Resources can be chosen as non-renewable (the maximum number of resources is the initial one), or as renewable (new resources appear with a certain tf rate), in which
In this case, fluctuations in the population number may occur, imposing the need to stop the simulation manually.

For calling the program run ``` python simulation.py ```

