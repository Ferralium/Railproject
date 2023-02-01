# Algorithms

**Random Algorithm**  
This algorithm is purely random. It chooses a starting station randomly, and moves randomly to the next station.

**Greedy Algorithm**  
The greedy algorithm is based on the random algorithm, however is not purely random. It chooses its starting station based on the amount of unused connection the stations have and will prioritise the station with the least amount of unused connections. For the move function, the greedy algorithm will choose the shortest connection that has not been used yet.
The logic behind this is that the first stations will all start at a station with only 1 connection. Since a train will choose an unused connection next, this algorithm will prevent connections with a dead end to be used twice. It is a greedy algorithm, as it will try to use as many conenctions as soon as possible. Choosing shorter connections means being able to use more connections in the limited time frame.

**Heuristic Algorithm**  
The heuristic algorithm is a skeleton to create your own algorithm. It takes a starting heuristic and a move heuristic and loops through them for as many runs as the user requires. This way, the user can use this algorithm to mix different starting and move functions, to find the optimal combination. It has also been made easy to create new starting and move functions individually, as they simply can be imported to the heuristic algorithm. Moreover, the structure of this algorithm has also been used in the Dijkstra and Simulated Annealing Algorithms, as the heuristics can be imported and tested.

**Simulated Annealing algorithm**  
The simulated annealing algorithm is a hillclimber algorithm that mutates the 2 last stations
of a train route. If this leads to an improvement in the overall quality, it will be implemented. If it
does not, the chance of it being implemented is 2 ^ (quality_old - quality_new). The bigger the
decrease in quality, the smaller the chance it will be implemented. There will be 20000 mutations for each run. However, the algorithm cuts of runs that are no improvement to the best run yet after 20, 100, 250 and 10000 mutations.

The simulated annealing algorithm contains an unidentified bug that incidentally causes the total time (min) to be lower than it truly is. For this reason, an if-statement is added in line 186 of main.py. This automatically breaks the loop when the total time is below 1552 (time needed to drive all the connections) and the proportion of visited routes is higher than 0.99. These situations together should not be possible. Despite this automatic break-off, the combination of start heuristic seven bridges (4) and move heuristic visited random (442) still lead to a false maximum quality. The same is true for the combination of start heuristic most connections (3) and move heuristic visited random. For this reason, these two combinations will not be considered in the results.

**Dijkstra Algorithm**  
The Dijkstra algorithm is a pathfinding algorithm that maps all nodes and finds the shortest route to all the nodes from a source node. It starts by initializing the correct values for the starting station and then maps outwards to find the shortest paths to all possible nodes. The algorithm uses a queue to keep track of the next steps and a visited list to keep track of the nodes that have already been processed. As it iterates through the nodes, it checks if the route length from the current path is better than the previous length and updates it if necessary. When all nodes have been processed, the algorithm writes a new dictionary with the most efficient routes. The new routes are used in combination with the start- and move heuristics to create an optimized solution.

The aim of the Dijkstra algorithm was to optimize the routes from a source node to all other nodes, potentially requiring less trains and thus minimizing the malus to the score that would be given. Unfortunately in combination with the move- and start heuristics it is less efficient than expected/hoped as the p function (fraction of driven lines) weighs heavily for the overall efficiency function of the RailNL case.
