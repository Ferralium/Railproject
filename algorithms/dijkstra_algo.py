from station import Station
import sys

class DijkstraAlgorithm:
    def __init__(self):
        # Takes the starting station (Most connections?) and finds the shortest route to all nodes. Aims to move from outside to inside
        # Routes with list from of connections to go from source station to the chosen destination
        self.oldroutes = {}
        self.correctroutes = {}

        # Dictionary containing the name of the station and the amount of time it takes to go to the station
        self.routescores = {}
        pass

    def find_shortest(self, source_station):
        """Maps all nodes and finds the shortest route to all the nodes from the source node
           Saves these routes for usage of the move function"""
        # Takes the source station and starts mapping outwards to find shortest paths to all possible
        self.oldroutes[source_station].connections
        pass

    def starting_station(self, station_dictionary, statnames):
        """Picks the starting station from a list of all possible stations
           Does this on the basis of the most connections"""
        self.oldroutes = station_dictionary
        highestcount = []
        # Picks station with the highest amount of connections
        for stations in self.oldroutes:
            if stations.connectioncount > highestcount[1]:
                highestcount = [stations.name, stations.connection_count]

        self.find_shortest(highestcount[0])
        pass  

    def move(self):
        """Moves to the next station along the precalculated route of the dijkstra algorithm
           When destination is reached, removes the line from possible lines"""
        pass