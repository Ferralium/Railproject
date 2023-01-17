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

import random
from station import Station
from train import Train
import pandas as pd
from typing import Any
from representatie import Mapdrawer


class Railsolver():

    # Initializes the stations dictionary for the railsolver
    def __init__(self) -> None:
        self.stations: dict[str, Station] = {}
        self.statnames: list[str] = []
        self.drawmod = Mapdrawer()

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


    def starting_station(self) -> Station:
        # first_number_connections = list(self.stations.values())[0]
        # highest_unused_connections = first_number_connections.connection_count
        # # highest_unused_connections = station_one.connection_count
        # all_stations_true: int = 0

        # voor het baseline algoritme wordt er een random station als beginstation gekozen
        current_station = random.choice(list(self.stations.values()))
        print(f'random starting station: {current_station}')
        return current_station

        # oude algoritme!!!!
        # checks if the station has 1 connection
        # if check_startingpoint is False or current_station.connection_count != 1:
        #     while current_station.connection_count != 1:
        #         starting_point = random.choice(self.statnames)
        #         current_station = self.stations.get(starting_point)
        #         check_startingpoint = all(station is True for station in current_station.connection_visited.values())
        #         if check_startingpoint is True and current_station.connection_count == 1:
        #             break
        #             break
        # #             starting_point = random.choice(self.statnames)
        # #             current_station = self.stations.get(starting_point)
        # #             break
        # # elif check_startingpoint is True and current_station.connection_count != 1:
        # #     while check_startingpoint is True:
        # #         starting_point = random.choice(self.statnames)
        # #         current_station = self.stations.get(starting_point)
        # #         check_startingpoint = all(station is True for station in current_station.connection_visited.values())
        # # elif check_startingpoint is True:
        # #     starting_point = random.choice(self.statnames)
        # #     current_station = self.stations.get(starting_point)
        # #     check_startingpoint = all(station is True for station in current_station.connection_visited.values())


    def move(self, current_station, train_stations):
        time = 0

        # voeg de current station toe aan de lijst
        train_stations.append(current_station)
        print(train_stations)

        while True:

            # Moves to next random connection that has not been visited yet
            possible_next_station: str | Station = random.choice(list(current_station.connections))
            next_station: Station = self.stations.get(possible_next_station)

            # Baseline: volgende station random (ook al is het al bezocht, mag je er heen)
            # daarom het deel hieronder uitgecommend

            # check_stations: bool = all(station is True for station in current_station.connection_visited.values())
            #
            # if check_stations is True:
            #     possible_next_station = random.choice(list(current_station.connections))
            #     next_station = self.stations.get(possible_next_station)
            # else:
            #     while current_station.is_visited(str(next_station)) is True:
            #         possible_next_station = random.choice(list(current_station.connection_visited))
            #         next_station = self.stations.get(possible_next_station)

            all_time: int = time + current_station.connections.get(str(next_station))

            # stops if time is more than 3 hours
            if all_time > 180:
                print(f'hi {all_time}')
                print(f'this will be returned {time}')
                return train_stations, time
            else:
                time = time + current_station.connections.get(str(next_station))

            print(f' Current Station: {current_station}')
            # check_startingpoint: bool = all(station is True for station in current_station.connection_visited.values())
            # print(check_startingpoint)
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))
            current_station: Station = self.stations.get(str(next_station))

            # voeg current_station toe aan de lijst
            train_stations.append(current_station)
            # print("treinstation toegevoegd")

            print(f' Next Station: {current_station}')
            print(time)
            print(" ")


    def quality_calc(self, fraction: float, list_of_numbers) -> None:
        T: int = list_of_numbers[1]
        Min: int = list_of_numbers[0]
        K: float = fraction*10000 - (T*100 + Min)

        print(f'Quality: {K} = {fraction}*1000 - ({T}*100 + {Min})')



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

            current_station: Station = wisselstoring.starting_station()

            list_of_stations_and_time: tuple[Station, int] = wisselstoring.move(current_station, train_stations)

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
        # Prints all stations on a map of the Netherlands
        self.drawmod.print_to_image()

        # Prints all connections between stations on a map of the Netherlands
        self.drawmod.print_connections()

        # Prints the driven routes with unique colors
        self.drawmod.print_driven_routes(routes)





if __name__ == '__main__':
    wisselstoring = Railsolver()
    wisselstoring.load_stations()

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
    wisselstoring.visualise(train_dictionary)
