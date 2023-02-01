# Heuristics

The algorithms 'Dijkstra', 'Simulated Annealing' and 'Heuristics' can be combined with the following start and move functions, of which some include a heuristic.
This program is also able to utilize the following combinations:

**Start heuristics:**

1. Random start heuristic: chooses a starting station completely randomly. This is technically not a heuristic, however we decided to add this one as a heurstic so it can be combined with other algorithms and heuristics.
2. Least connections start heuristic: chooses a starting station with the least connections that have not been used yet
3. Most connections start heuristic: chooses a starting station with the most connections that have not been used yet
4. Seven bridges start heuristic: chooses a starting station that has an uneven number of connections that have not been used yet

**Move heuristics:**

1. Random move heuristic: chooses randomly which connection to use next. This one is also not a true heuristic, but very useful to have for the experiments and to run combined with other heuristics and algorithms.
2. Visited random move heuristic: chooses randomly which connection to use next, with the constraint that the connection has not been used yet
3. Shortest move heuristic: chooses the shortest connection, with the constraint that the connection has not been used yet
4. Preference shortest move heuristic: gives a preference that weights 70%, to choose the shortest connection, with the constraint that the connection has not been used yet
