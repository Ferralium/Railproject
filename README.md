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
* Wisselstoring: this is the main folder where you can navigate to other folders and read the text files.
* Code: this is the main folder containing all the python code files, including the main.py. In the code folder you can find the following 2 folders as well:
    * algorithms: containing all the different algorithms.
    * heuristics: containg the heuristics in different files.
* Data: this folder contains the important csv files with the data about the trains station and connections.
* Gifgen: This folder will hold images of all the seperate routes, after running the code.
* Images: After running the code, this folder contains the maps with the train stations and the connections. Moreover, it has a gif that has the routes of the trajectories animated.
* Results: The results of the trajectories will be exported to csv files, that will show up in this folder after running the code.


# Algorithms:
This program has the ability to run  different algorithms, each providing  seperate output for comparison.
These algorithms can be found in the folder Algorithms (Wisselstoring/Code/algorithms).

### Types of algorithms:
The following algorithms are used:
1. Random Algorithm
2. Greedy Algorithm
3. Heuristic Algorithm
4. Simulated Annealing Algorithm
5. Dijkstra Algorithm

**Simulated Annealing algorithm**
The simulated annealing algorithm is a hillclimber algorithm that mutates the 2 last stations
of a train route. If this leads to an improvement in the overall quality, it will be implemented. If it
does not, the chance of it being implemented is 2 ^ (quality_old - quality_new). The bigger the
decrease in quality, the smaller the chance it will be implemented.

The simulated annealing algorithm contains an unidentified bug that causes the fraction of visited
connections to be higher than it truly is. Therefore, two if-statements are used to break the current
run when this happens. This happens when the total amount of minutes is lower than 1488, and if the
quality is higher than 6800 (no valid scores have been seen above this point). If either of these
if-statements applies, the current run is broken off and will not be saved for the overall score.
Please note that these if-statements may not break all incorrect scores. In addition, they may break some
correct scores. This could influence the results.

### Usage:
By default the program is run with the following command:

"""
python3 main.py
"""

This will run the program for 1 run, using the random algorithm.

To run this program for multiple runs please use the following command:

"""
python3 main.py a n (Example: python3 main.py 500 1)
"""

Where a is the amount of runs (1 - ∞) and n is the algorithm selector (1 - 5, as seen in types of algorithms)

# Heuristics:
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

"""
python3 main.py a n s m (Example: python3 main.py 500 1 3 3)
"""

Where s is the start heuristic (1-4) and m is the move heuristic (1-4)

# Histogram:
Automatically when running the program, the quality of every run is being saved in a seperate file in the folder "results". In order to generate a histogram, the user can use the following commandline:

"""
python3 histogram.py
"""

The question "which score?" will pop up. The user can fill in the combination of numbers of the result file they wish to use for the histogram.

For instance for the following combination, a resultsfile named "score322.txt" will be created.

"""
python3 main.py 1 3 2 2
"""

The user can call the histogram.py and answer the question with "322", and a histogram based on the information in the score322 file will be created.

By answering "stop" the program will stop running, untill then the user can request as many histograms as there are result files.

# Experiments:
For our experiments we ran each algorithm (In combination with heuristics where applicable) for 5000 times. As there are 50 possible combinations we will simply summarize the best findings for each algorithm. To perform your own tests, please see

**Best combinations:**

Random algorithm(1): Mean 1981 Highest 2741
Greedy algorithm(2): Mean 4455 Highest 4655
Heurisitc algorithm, Least connections start, Visited random move (322): Mean 6108 Highest 7020
Simulated Annealing(4), Seven bridges start Heuristic, Preference shortest move heuristic (442), Mean 5867
Dijkstra algorithm,

# Discussion:

In theory, the highest possible score is 7549. It requires 1551 minutes to visit all connections. For this, you need 9 trains.
This yields the formula: K = p*10000 - (T*100 + Min) =  1 * 10000 - (9 * 100 + 1551) = 7549.

Using a complete random algorithm, we found that the mean score produced was 1981. The algorithms we created produce scores somewhere between the values above, with a top score of 7020. This is approaching the maximum score.
