# Wissselstoring
This project contains a python program which aims to provide the most optimal solution for rail routing across the Netherlands.
It does this by implementing several algorithms and heuristics with the aim of providing the most optimal solution for the routes.
Additionally, this program provides the option of visualising the routes in .PNG, .GIF format and can create insights in histogram form on the solutions.

# Getting started:
To get started, some actions are required. First, multiple python packages are required for the program to run. These can be installed by using the following command:
"""
pip install -r requirements.txt
"""

# Outline:
After downloading the code, you will find the files divided into multiple folders.
TODO: Folders fixen en uitleg geven

# Algorithms:
This program has the ability to run  different algorithms, each providing  seperate output for comparison.
These algoirthms can be found in ...

### Types of algorithms:
The following algorithms are used:
1. Random Algorithm
2. Greedy Algorithm
3. Heuristic Algorithm
4. Simulated Annealing Algorithm
5. Dijkstra Algorithm

### Usage:
By default the program is run with the following command:
"""
python3 main.py
"""
This will run the program for 1 run, using the random algorithm.

To run this program for multiple runs please use the following command:
"""
python3 main.py a n (Example: python3 main.py 1 500)
"""
Where a is the algorithm selector (1 - 5, as seen in types of algorithms) and n is the amount of runs (1 - ∞)

### Heuristics:
This program is also able to utilize the following heuristics:
**Start heuristics:**
1. Random start heuristic
2. Least connections start heuristic
3. Most connections start heuristic
4. Seven bridges start heuristic

**Move heuristics:**
1. Random move heuristic
2. Visited random move heuristic
3. Shortest move heuristic
4. Preference shortest move heuristic

For  algorithms 3-5 heuristics have to be selected. This can be done using the following command:
"""
python3 main.py a n s m (Example: python3 main.py 1 500 3 3)
"""
Where s is the start heuristic (1-4) and m is the move heuristic (1-4)

# Experiments:


