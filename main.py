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
# import workbook
# import openpyxl
# from csv import DictWriter

class Railsolver():

    # Initializes the stations dictionary for the railsolver
    def __init__(self):
        self.stations = {}
        self.statnames = []

        # Trein nummer voor trein klasse die route pakt en de afstand bijhoudt
        self.traincount = 1

    def load_stations(self):
        """Loads the stations with distances from the CSV.
           Also creates new stations for the connections if they are not already in the dict"""

        with open('data/ConnectiesHollandKlein.csv') as f:
            # Met de next functie wordt de eerste lijn overgeslagen, dit geeft alleen informatie over de inhoud
            next(f)

            # For loop iterates over the lines in the csv and modifies them to usable format
            for line in f:
                templine = line
                templine = templine.strip().split(',')

                # Adds unique station names to list to select random point later
                for i in range(2):
                    if templine[i] not in self.statnames:
                        self.statnames.append(templine[i])

                # !!!Samenvoegen in enkele for loop, die zowel source als destination station checkt?!!!

                # Checks if station already exists, if so adds connection
                if templine[0] in self.stations:
                    self.stations[templine[0]].add_station(templine[1], int(templine[2]))

                # If the station does not exist initializes the station and adds the connection
                elif templine[0] not in self.stations:
                    self.stations[templine[0]] = Station(templine[0])
                    self.stations[templine[0]].add_station(templine[1], int(templine[2]))

                # Checks whether the connection already exists in the stations and adds it if this is not the case
                if templine[1] not in self.stations:
                    self.stations[templine[1]] = Station(templine[1])
                    self.stations[templine[1]].add_station(templine[0], int(templine[2]))

                elif templine[1] in self.stations:
                    self.stations[templine[1]].add_station(templine[0], int(templine[2]))

    def routecalc(self, train_stations):
        time = 0
        lowest_unused_connections = 100
        all_stations_true = 0

        for station in self.stations:
            print(station)
            check_connections = self.stations.get(station)
            check_startingpoint = all(station is True for station in check_connections.connection_visited.values())
            possible_current_station = self.stations.get(str(check_connections))

            if check_startingpoint is True:
                all_stations_true += 1

            if check_connections.connection_count == 1:
                    if check_startingpoint is False:
                        current_station = self.stations.get(str(possible_current_station))
                        break
            elif check_connections.connection_count != 1 or check_startingpoint == False:
                # possible_current_station = self.stations.get(str(check_connections))
                unused_connections = 0
                for connections in possible_current_station.connection_visited.values():
                    # print(connections)
                    if connections == False:
                        unused_connections += 1
                print(unused_connections)
                if unused_connections < lowest_unused_connections and unused_connections != 0:
                    lowest_used_connections = unused_connections
                    current_station = self.stations.get(str(possible_current_station))

        print(len(self.stations))
        print(all_stations_true)
        if all_stations_true is len(self.stations):
            starting_point = random.choice(self.statnames)
            current_station = self.stations.get(starting_point)

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

        # voeg de current station toe aan de lijst
        train_stations.append(current_station)

        while True:

            # Moves to next random connection that has not been visited yet
            possible_next_station = random.choice(list(current_station.connections))
            next_station = self.stations.get(possible_next_station)

            check_stations = all(station is True for station in current_station.connection_visited.values())

            if check_stations is True:
                possible_next_station = random.choice(list(current_station.connections))
                next_station = self.stations.get(possible_next_station)
            else:
                while current_station.is_visited(str(next_station)) is True:
                    possible_next_station = random.choice(list(current_station.connection_visited))
                    next_station = self.stations.get(possible_next_station)

            time = time + current_station.connections.get(str(next_station))

            # stops if time is more than 2 hours
            if time > 120:
                return train_stations

            print(f' Current Station: {current_station}')
            check_startingpoint = all(station is True for station in current_station.connection_visited.values())
            print(check_startingpoint)
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))
            current_station = self.stations.get(str(next_station))

            # voeg current_station toe aan de lijst
            train_stations.append(current_station)
            # print("treinstation toegevoegd")

            print(f' Next Station: {current_station}')
            print(time)
            print(" ")

            # K = p*10000 - (T*100 + Min)

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

        # final_total = round(total / 2)
        # final_connected = round(total / 2)

        print(f' Connected: {connected}, Total: {total}')
        fraction: float = round(connected / total, 2)
        return fraction


    def table_of_trains(self, train_number, list_of_stations, train_dictionary):
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




if __name__ == '__main__':
    wisselstoring = Railsolver()
    wisselstoring.load_stations()

    # maak een lege dictionary waarin de treinen worden opgeslagen
    train_dictionary: dict[str, list[Station]] = {}

    for route in range(7):

        # maak de treinnaam
        train_number = "train_" + str(route + 1)

        # maak een lege lijst voor de stations:
        train_stations = []

        print(" ")
        print("new trajectory")

        list_of_stations = wisselstoring.routecalc(train_stations)
        # print(list_of_stations)

        # voeg dit toe aan de tabel van treinen
        wisselstoring.table_of_trains(train_number, list_of_stations, train_dictionary)

    print(wisselstoring.fraction_calc())
    # while all_connections != 56:
    #     for route in range(7):
    #         print(" ")
    #         print("new trajectory")
    #         wisselstoring.routecalc()
    #     all_connections = wisselstoring.fraction_calc()
