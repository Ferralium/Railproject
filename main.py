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
        print(current_station)

        # makes sure the starting trajectory is new
        check_startingpoint = all(station is True for station in current_station.connection_visited.values())
        print(check_startingpoint)
        if check_startingpoint is True:
            while check_startingpoint is True:
                starting_point = random.choice(self.statnames)
                current_station = self.stations.get(starting_point)
                check_startingpoint = all(station is True for station in current_station.connection_visited.values())
                print(current_station)
                print(check_startingpoint)

        while True: # moet een andere while statement - totdat alle connecties zijn geweest
            print(current_station)
            print(current_station.connections)

            # Moves to next random connection that has not been visited yet
            next_station = random.choice(list(current_station.connections))

            check_stations = all(station is True for station in current_station.connection_visited.values())
            print(check_stations)

            if check_stations is True:
                next_station = random.choice(list(current_station.connections))
            else:
                while current_station.is_visited(next_station) is True:
                    next_station = random.choice(list(current_station.connection_visited))

            time = time + current_station.connections.get(next_station)

            # stops if time is more than 2 hours
            if time > 120:
                break

            # sets the station as visited
            current_station.stationvisit(next_station)
            current_station = self.stations.get(next_station)

            print(current_station)
            print(time)
            print(" ")
            print("next connection")

            # K = p*10000 - (T*100 + Min)


if __name__ == '__main__':
    wisselstoring = Railsolver()
    wisselstoring.load_stations()
    for route in range(7):
        print(" ")
        print("new trajectory")
        wisselstoring.routecalc()
