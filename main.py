"""
    railsolver.py

    Door:
        Chiara Schut - 2955520
        Berber Siersma - 
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

        while time < 120:
            print(current_station)

            # sets the station as visited
            current_station.stationvisit(current_station)
    
            # Checks next possible stations
            possible_connections = current_station.connections
            print(current_station.connections)

            # Moves to next random connection that has not been visited yet
            next_station = random.choice(list(current_station.connections))
            print(next_station)

            # wat als de connectie nog een keer gebruikt moet worden?
            while current_station.is_visited(next_station) is True or current_station == next_station:
                next_station = random.choice(list(current_station.connection_visited))

            time = time + current_station.connections.get(next_station)
            current_station = self.stations.get(next_station)
            
            print(current_station)
            print(time)
            # bewegen naar nieuw station lukt, alleen pakt hij niet current_Station als True

            # NIET relevant!!!!!!
            # searches for the conenction with the lowest time travel
            # for station in current_station.connection_visited:
            #     distance = int(current_station.connections.get(station))
            #     distance_score = distance
            #     if distance <= distance_score:
            #         next_station = station
            #         distance_score = distance


if __name__ == '__main__':
    wisselstoring = Railsolver()
    wisselstoring.load_stations()
    wisselstoring.routecalc()