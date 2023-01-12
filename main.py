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

    def routecalc(self):
        time = 0
        # Determine start point and from there make route
        starting_point = random.choice(self.statnames)
        current_station = self.stations.get(starting_point)
        print(f' Startpunt: {current_station}')

        # ideas for algorithm:
        # Starting point: makes sure the starting trajectory is a station with only 1 connection (dordrecht + den helder)
        # starting point: starting with the stations with the least connections (omgekeerde van greedy)

        # makes sure the starting trajectory is new 
        check_startingpoint = all(station is True for station in current_station.connection_visited.values())
        print(check_startingpoint)
        # print(current_station.connection_visited.keys())

        # checks if the station has 1 connection
        if check_startingpoint is False or current_station.connection_count != 1:
            while current_station.connection_count != 1:
                starting_point = random.choice(self.statnames)
                current_station = self.stations.get(starting_point)
                check_startingpoint = all(station is True for station in current_station.connection_visited.values())
                if check_startingpoint is True and current_station.connection_count == 1:
                    starting_point = random.choice(self.statnames)
                    current_station = self.stations.get(starting_point)
                # while check_startingpoint is True:
                #     # in deze loop gaat t fout
                #     starting_point = random.choice(self.statnames)
                #     current_station = self.stations.get(starting_point)
                #     check_startingpoint = all(station is True for station in current_station.connection_visited.values())
                #     print(current_station)
                #     print(check_startingpoint)
        elif check_startingpoint is True:
            starting_point = random.choice(self.statnames)
            current_station = self.stations.get(starting_point)
            # if current_station.connection_count == 1:
            #     starting_point = random.choice(self.statnames)
            #     current_station = self.stations.get(starting_point)
            # else:
            #     while check_startingpoint is Tru:
            #         starting_point = random.choice(self.statnames)
            #         current_station = self.stations.get(starting_point)
            #         check_startingpoint = all(station is True for station in current_station.connection_visited.values())
            #         print(current_station)
            #         print(check_startingpoint)

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
                break
            
            print(f' Current Station: {current_station}')
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))
            current_station = self.stations.get(str(next_station))

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


if __name__ == '__main__':
    wisselstoring = Railsolver()
    wisselstoring.load_stations()
    for route in range(7):
        print(" ")
        print("new trajectory")
        wisselstoring.routecalc()
    print(wisselstoring.fraction_calc())
    # while all_connections != 56:
    #     for route in range(7):
    #         print(" ")
    #         print("new trajectory")
    #         wisselstoring.routecalc()
    #     all_connections = wisselstoring.fraction_calc() 
