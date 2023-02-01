# Heuristics

The algorithms 'Dijkstra', 'Simulated Annealing' and 'Heuristics' can be combined with the following start and move functions, of which some include a heuristic.
This program is also able to utilize the following heuristics:

**Start heuristics:**
1. Random start heuristic: chooses a starting station completely randomly
2. Least connections start heuristic: chooses a starting station with the least connections that have not been used yet
3. Most connections start heuristic: chooses a starting station with the most connections that have not been used yet
4. Seven bridges start heuristic: chooses a starting station that has an uneven number of connections that have not been used yet

**Move heuristics:**
1. Random move heuristic: chooses randomly which connection to use next
2. Visited random move heuristic: chooses randomly which connection to use next, with the constraint that the connection has not been used yet
3. Shortest move heuristic: chooses the shortest connection, with the constraint that the connection has not been used yet
4. Preference shortest move heuristic: gives a preference that weights 70%, to choose the shortest connection, with the constraint that the connection has not been used yet

For  algorithms 3-5 heuristics have to be selected. This can be done using the following command:

``` python3 main.py a n s m (Example: python3 main.py 500 1 3 3) ```

Where s is the start heuristic (1-4) and m is the move heuristic (1-4)