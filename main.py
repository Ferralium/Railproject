"""
    railsolver.py
    Door:
        Chiara Schut - 14676869
        Berber Siersma - 14472295
        Jeroen Steenhof - 12709425
    Minor Programmeren - Algoritmen en Heuristieken
    Attempts to solve heuristic problem with train stations.
"""
# TYPEHINTS!!! DOCSTRINGS!! COMMENTS!!!

import time
import random
from algorithm import Algorithm
from station import Station
# from train import Train
import pandas as pd
from typing import Any
from representatie import Mapdrawer, Gifgenerator
import sys

from algorithms.random_algo  import RandomAlgorithm
from algorithms.simulatedannealing import SimulatedAnnealing
from algorithms.GreedyAlgorithm import GreedyAlgorithm
from algorithms.heuristic_algorithm import HeuristicAlgorithm
from algorithms.dijkstra_algo import DijkstraAlgorithm
from heuristics.start_least_connections import least_connection_start_heuristic
from heuristics.start_most_connections import most_connection_start_heuristic
from heuristics.start_random import random_start_heuristic
from heuristics.start_7bridges import sevenbridges_start_heuristic
from heuristics.move_random import random_move_heuristic
from heuristics.move_visited_random import visited_random_move_heuristic
from heuristics.move_shortest import shortest_move_heuristic
from heuristics.move_shortest_preference import preference_shortest_move_heuristic


class Railsolver():

    # Initializes the stations dictionary for the railsolver
    def __init__(self, algorithm: Algorithm) -> None:
        self.stations = {}
        self.statnames = []
        self.load_stations()
        self.algo = algorithm

        # Trein nummer voor trein klasse die route pakt en de afstand bijhoudt
        self.traincount: int = 1

    def load_stations(self) -> None:
        """Loads the stations with distances from the CSV.
           Also creates new stations for the connections if they are not already in the dict"""

        with open('data/ConnectiesNationaal.csv') as f:
            # Met de next functie wordt de eerste lijn overgeslagen, dit geeft alleen informatie over de inhoud
            next(f)

            # For loop iterates over the lines in the csv and modifies them to usable format
            for line in f:
                templine: str = line
                # ik denk dat we deze een andere variabele naam moeten geven, anders werkt de typehint niet.
                templine = templine.strip().split(',')

                # Adds unique station names to list to select random point later
                for i in range(2):
                    if templine[i] not in self.statnames:
                        self.statnames.append(templine[i])

                # !!!Samenvoegen in enkele for loop, die zowel source als destination station checkt?!!!

                # Checks if station already exists, if so adds connection
                if templine[0] in self.stations:
                    self.stations[templine[0]].add_station(templine[1], float(templine[2]))

                # If the station does not exist initializes the station and adds the connection
                elif templine[0] not in self.stations:
                    self.stations[templine[0]] = Station(templine[0])
                    self.stations[templine[0]].add_station(templine[1], float(templine[2]))

                # Checks whether the connection already exists in the stations and adds it if this is not the case
                if templine[1] not in self.stations:
                    self.stations[templine[1]] = Station(templine[1])
                    self.stations[templine[1]].add_station(templine[0], float(templine[2]))

                elif templine[1] in self.stations:
                    self.stations[templine[1]].add_station(templine[0], float(templine[2]))

    def quality_calc(self, fraction: float, list_of_numbers) -> None:
        T: int = list_of_numbers[1]
        Min: int = list_of_numbers[0]
        self.K: float = fraction*10000 - (T*100 + Min)
        self.quality = f'Quality: {self.K} = {fraction}*1000 - ({T}*100 + {Min})'
        print(self.quality)

    def fraction_calc(self) -> float:
        """ Function calculates percentage of used connections """

        print("Calculate franction of used connections")
        print()
        connected = 0
        total = 0

        for station_name in self.stations:

            temporary_station = self.stations[station_name]

            # print(station_name, temporary_station.connection_visited)
            # number_of_connections = len(temporary_station.connection_visited)
            number_of_connections = len(temporary_station.connections)
            # print(f'aantal connecties: {number_of_connections}')
            total += number_of_connections

            for connecties in temporary_station.connection_visited:

                if temporary_station.connection_visited[connecties] == True:
                    connected += 1

        print(f' Connected: {connected}, Total: {total}')
        fraction: float = round(connected / total, 2)

        return fraction

    def table_of_trains(self, train_number, list_of_stations, time, train_dictionary):
        """ Function that keeps track of all the train routes that have been made """

        # voeg de trein en stations toe aan de dictionary
        train_dictionary[train_number] = list_of_stations

        train_data = pd.DataFrame.from_dict(train_dictionary, orient='index')
        print(train_data)

        data_to_excel = pd.ExcelWriter('train_data.xlsx')

        # write DataFrame to excel
        train_data.to_excel(data_to_excel)

        # save the excel
        data_to_excel.save()

    def take_a_ride(self):
        """ Function that keeps the order of everything that must be done for the algorithm
        (less in the main) """
        total_time: int = 0
        number_of_routes: int = 0
        total_time_each_train = {}

        for route in range(20):

            # number_of_routes += 1

            # maak de treinnaam
            train_number: str = "train_" + str(route + 1)

            # maak een lege lijst voor de stations:
            train_stations: list[Station] = []

            print(" ")
            print("new trajectory")

            current_station: Station = self.algo.starting_station(self.stations, self.statnames)

            list_of_stations_and_time: tuple[Station, int] = self.algo.move(current_station, train_stations, self.stations)
            total_time_each_train[train_number] = list_of_stations_and_time[1]
            print(list_of_stations_and_time)

            check_station = list_of_stations_and_time[0]
            print(check_station)
            if check_station == [None]:
                break
            else:

                # voeg dit toe aan de tabel van treinen
                wisselstoring.table_of_trains(train_number, *list_of_stations_and_time, train_dictionary)

                time_trajectory: int = list_of_stations_and_time[1]

                # add total time of all trajectories
                total_time += time_trajectory

                number_of_routes += 1

        list_of_numbers: list[int] = [total_time, number_of_routes]
        print(f'list of numbers: {list_of_numbers}')
        return list_of_numbers, total_time_each_train




    def loop_simulated_annealing(self, train_dictionary):
        """ Loop that controls the simmulated annealing process """

        # train_dictionary = {}
        list_of_numbers, total_time_each_train = wisselstoring.take_a_ride()

         # bereken de fractie van de bereden routes
        fraction: float = wisselstoring.fraction_calc()
        quality_old = self.algo.quality_calc(fraction, list_of_numbers)
        print(quality_old)

        # loop met opgedeelde mutation functies
        for i in range(20):
            #check

            # kondig nieuwe loop aan:
            print()
            print("make a mutation: ")
            print()

            train_dictionary_2 = train_dictionary
            stations_library = wisselstoring.stations

            switching_stations, chosen_one = self.algo.stations_to_be_switched(train_dictionary_2, stations_library, total_time_each_train)

            change_in_time = self.algo.mutation_small(train_dictionary_2, train_dictionary, switching_stations, chosen_one, stations_library)

            # bereken nu opnieuw de totale tijd voor de treinen

            print(f'min oud: {list_of_numbers[0]}')
            list_of_numbers[0] += change_in_time
            print(f'min update: {list_of_numbers[0]}')
              # bereken de fractie van de bereden routes
            fraction: float = wisselstoring.fraction_calc()
            quality_2 = self.algo.quality_calc(fraction, list_of_numbers)
            print(f'quality oud: {quality_old}')
            print(f'quality 2: {quality_2}')

            # vergelijk nu deze met elkaar, en is het beter of de kans zegt dat het moet, verander hem dan
            short_tuple, mutated = self.algo.make_or_break_change(quality_old, quality_2, train_dictionary, train_dictionary_2, change_in_time, list_of_numbers, total_time_each_train, chosen_one)

            train_dictionary = short_tuple[0]
            quality_old = short_tuple[1]

            if mutated == False:
                #check
                # zet dan ook de connection visits weer terug
                self.algo.reset_visiting_status(switching_stations, stations_library)


        # loop met mutaties
        # for i in range(10):
        #
        #     train_dictionary_2 = train_dictionary
        #     stations_library = wisselstoring.stations
        #
        #     switching_stations, chosen_one = self.algo.stations_to_be_switched(train_dictionary_2, stations_library)
        #     # list_of_numbers = wisselstoring.take_a_ride()
        #     change_in_time = self.algo.mutation_small(train_dictionary_2, train_dictionary, switching_stations, chosen_one, stations_library)
        #
        #     # bereken nu opnieuw de totale tijd voor de treinen
        #
        #     list_of_numbers[0] += change_in_time
        #     # bereken de fractie van de bereden routes
        #     fraction: float = wisselstoring.fraction_calc()
        #     quality_2 = self.algo.quality_calc(fraction, list_of_numbers)
        #
        #     # vergelijk nu deze met elkaar, en is het beter of de kans zegt dat het moet, verander hem dan
        #     short_tuple, mutated = self.algo.make_or_break_change(quality_old, quality_2, train_dictionary, train_dictionary_2, change_in_time, list_of_numbers)
        #
        #     train_dictionary = short_tuple[0]
        #     quality = short_tuple[1]
        #
        #     if mutated == False:
        #           # zet dan ook de connection visits weer terug
        #           self.algo.reset_visiting_status(switching_stations, stations_library)



    def visualise(self, routes):
        """Uses the map visualisation module to create multiple images of the state of the map."""
        # Initializes the map
        self.drawmod = Mapdrawer()

        # Prints all stations on a map of the Netherlands
        self.drawmod.print_to_image()

        # Prints all connections between stations on a map of the Netherlands
        self.drawmod.print_connections()

        # Prints the driven routes with unique colors
        self.drawmod.print_driven_routes(routes)

        # Initializes gif generator
        self.gifmod = Gifgenerator()


def select_heuristic(start_heurselect, move_heurselect):
    start_heuristic = None
    if start_heurselect == 1:
        start_heuristic = random_start_heuristic
    elif start_heurselect == 2:
        start_heuristic = least_connection_start_heuristic
    elif start_heurselect == 3:
        start_heuristic = most_connection_start_heuristic
    elif start_heurselect == 4:
        start_heuristic = sevenbridges_start_heuristic

    if move_heurselect == 1:
        return start_heuristic, random_move_heuristic
    elif move_heurselect == 2:
        return start_heuristic, visited_random_move_heuristic
    elif move_heurselect == 3:
        return start_heuristic, shortest_move_heuristic
    elif move_heurselect == 4:
        return start_heuristic, preference_shortest_move_heuristic


if __name__ == '__main__':
    start_time = time.time()
    algoselect = 4
    start_heuristic = None
    move_heuristic = None

    best_solution = {}
    best_score = 0
    best_calc = ''
    mean_solution = 0
    num_of_runs = 1
    histoscore = []


    file1 = open('results/resultsformula.txt', 'w')
    file1.close()
    file2 = open('results/score.txt', 'w')
    file2.close()



    if len(sys.argv) > 1:
        if not sys.argv[1].isnumeric():
            print('Usage: python3 main.py (Optional) n')
            sys.exit()
        num_of_runs = int(sys.argv[1])
        if num_of_runs < 1:
            print('Usage: python3 main.py (Optional) n')
            print('Number of runs must be 1 or higher')
            sys.exit()

        if len(sys.argv) > 2:
            if not sys.argv[2].isnumeric():
                print('Usage: python3 main.py (1 -> n) n (1 -> x) algorithm')
                sys.exit()
            algoselect = int(sys.argv[2])
            #
            #
            # deze tussen 1 en 8 hieronder nog veranderen naar het aantal van algoselect we op het einde hebben
            if algoselect < 1 or algoselect > 5:
                print('Usage: python3 main.py (1 -> n) n (1 -> x) algorithm')
                print('Algorithm must be between 1 and 8')
                sys.exit()

            if algoselect == 3 or algoselect == 5:
                if len(sys.argv) < 5 or not sys.argv[3].isnumeric() or not sys.argv[4].isnumeric():
                    print('Usage: python3 main.py (1 -> n) n (1 -> x) algorithm (1 -> x) start_heuristic move_heuristic')
                    sys.exit()
                start_heurselect = int(sys.argv[3])
                move_heurselect = int(sys.argv[4])
                if start_heurselect < 1 or start_heurselect > 4 or move_heurselect < 1 or move_heurselect > 4:
                    print('Usage: python3 main.py (1 -> n) n (1 -> x) algorithm (1 -> x) start_heuristic move_heuristic')
                    print('Heuristic must be between 1 and 4')
                    sys.exit()
                start_heuristic, move_heuristic = select_heuristic(start_heurselect, move_heurselect)


    # command-line
    if algoselect == 1:
        algo = RandomAlgorithm()
    elif algoselect == 2:
        algo = GreedyAlgorithm()
    elif algoselect == 3:
        algo = HeuristicAlgorithm(start_heuristic, move_heuristic)
    elif algoselect == 4:
        algo = SimulatedAnnealing()
    elif algoselect == 5:
        algo = DijkstraAlgorithm(start_heuristic, move_heuristic)


    train_dictionary = {}

    # simulated annealing loop:
    #
    #
    # deze if else loop kan niet... ik denk wat je onder if algoselect = 7 hebt, dat je het beter hierboven kan toevoegen eronder. Nu als je ieats anders op commandline doet geeft hij niet meer de goede errorS
    if algoselect == 4:
        wisselstoring = Railsolver(algo)
        print("simulated annealing")
        Railsolver(algo).loop_simulated_annealing(train_dictionary)
    else:
        for i in range(num_of_runs):
            wisselstoring = Railsolver(algo)

            # maak een lege dictionary waarin de treinen worden opgeslagen
            train_dictionary = {}
            # number_of_routes: int = 0
            # total_time: int = 0

            list_of_numbers, total_time_each_train = wisselstoring.take_a_ride()

            # bereken de fractie van de bereden routes
            fraction: float = wisselstoring.fraction_calc()
            wisselstoring.quality_calc(fraction, list_of_numbers)
            mean_solution += wisselstoring.K

            if wisselstoring.K > best_score:
                best_score = wisselstoring.K
                best_solution = train_dictionary
                best_calc = wisselstoring.quality

            results = open('results/resultsformula.txt', 'a')
            results.write(f'{wisselstoring.quality}')
            results.write('\n')
            results.close()

            score = open('results/score.txt', 'a')
            score.write(str(wisselstoring.K))
            score.write('\n')
            score.close()


            # print(wisselstoring.algo.prunedroutes.keys())

        wisselstoring.visualise(best_solution)
        wisselstoring.gifmod.map_to_gif()
        print(f'Best solution found: {best_calc}')
        print(f'Average soluton: {mean_solution / num_of_runs}')
        print(f'Runtime: {time.time() - start_time}')
