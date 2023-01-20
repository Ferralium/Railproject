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
from station import Station
from train import Train
import pandas as pd
from typing import Any
from representatie import Mapdrawer, Gifgenerator
import sys
from algorithms.random_algo  import RandomAlgorithm
from algorithms.smart_algo import SmartAlgorithm

class Railsolver():

    # Initializes the stations dictionary for the railsolver
    def __init__(self, stations, statnames, algonum) -> None:
        self.stations =  stations
        self.statnames = statnames
        self.algoselector = algonum

        # Selects and implements the algorithm for the railsolver
        self.algorithm_selection()

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

        return self.stations, self.statnames

    def algorithm_selection(self):
        if self.algoselector == 1:
            self.algo = RandomAlgorithm()
        elif self.algoselector == 2:
            self.algo = SmartAlgorithm()

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

        for route in range(20):

            number_of_routes += 1

            # maak de treinnaam
            train_number: str = "train_" + str(route + 1)

            # maak een lege lijst voor de stations:
            train_stations: list[Station] = []

            print(" ")
            print("new trajectory")

            current_station: Station = self.algo.starting_station(self.stations, self.statnames)

            list_of_stations_and_time: tuple[Station, int] = self.algo.move(current_station, train_stations, self.stations)

            # voeg dit toe aan de tabel van treinen
            wisselstoring.table_of_trains(train_number, *list_of_stations_and_time, train_dictionary)

            time_trajectory: int = list_of_stations_and_time[1]

            # add total time of all trajectories
            total_time += time_trajectory

        list_of_numbers: list[int] = [total_time, number_of_routes]
        print(f'list of numbers: {list_of_numbers}')
        return list_of_numbers

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

if __name__ == '__main__':
    start_time = time.time()
    statconnectlib = {}
    statnamelib = []
    algoselect = 1

    wisselstoring = Railsolver(statconnectlib, statnamelib, algoselect)
    statconnectlib, statnamelib = wisselstoring.load_stations()
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


    
    if len(sys.argv) >= 2:
        if sys.argv[1].isnumeric() == False:
            print('Usage: python3 main.py (Optional) n')
            sys.exit()
        if int(sys.argv[1]) > 1:
            num_of_runs = int(sys.argv[1])
        if len(sys.argv) >= 3:
            if sys.argv[1].isnumeric() == False and sys.argv[2].isnumeric() == False:
                print('Usage: python3 main.py (1 -> n) n (1 -> x) algorithm')
            if int(sys.argv[2]) > 1:
                algoselect = int(sys.argv[2])


    for i in range(num_of_runs):
        wisselstoring = Railsolver(statconnectlib, statnamelib, algoselect)

        # maak een lege dictionary waarin de treinen worden opgeslagen
        train_dictionary = {}
        # number_of_routes: int = 0
        # total_time: int = 0

        list_of_numbers = wisselstoring.take_a_ride()

        # dit stuk naar een functie !
        # for route in range(7):
        #
        #     number_of_routes += 1
        #
        #     # maak de treinnaam
        #     train_number: str = "train_" + str(route + 1)
        #
        #     # maak een lege lijst voor de stations:
        #     train_stations: list[Station] = []
        #
        #     print(" ")
        #     print("new trajectory")
        #
        #     current_station: Station = wisselstoring.starting_station()
        #
        #     list_of_stations_and_time: tuple[Station, int] = wisselstoring.move(current_station, train_stations)
        #
        #     # voeg dit toe aan de tabel van treinen
        #     wisselstoring.table_of_trains(train_number, *list_of_stations_and_time, train_dictionary)
        #
        #     time_trajectory: int = list_of_stations_and_time[1]
        #
        #     # add total time of all trajectories
        #     total_time += time_trajectory
        #
        # print(f'total time {total_time}')

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

    # wisselstoring.visualise(best_solution)
    # wisselstoring.gifmod.map_to_gif()
    print(f'Best solution found: {best_calc}')
    print(f'Average soluton: {mean_solution / num_of_runs}')
    print(f'Runtime: {time.time() - start_time}')