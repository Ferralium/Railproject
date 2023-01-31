from station import Station
from heuristics.start_most_connections import most_connection_start_heuristic


# Head fix
class DijkstraAlgorithm:
    def __init__(self, start_heuristic, move_heuristic):
        """Dijkstra Algorithm aims to create a minimum spanning tree with the lowest cost distances
           to all points in the map from a single source station"""
        # Keeps track of whether the MST has been generated yet
        self.gencount = 0
        
        # Keeps the old dictionary with all the routes for safekeeping
        self.oldroutes = {}

        # Imports the heuristics and saves them for further use
        self.start_heuristic = start_heuristic
        self.move_heuristic = move_heuristic

        # Variables to keep track of the newly calculated routes
        self.newroute = {}
        self.distance_to = {}

        for station in self.oldroutes:
            self.distance_to[station] = float('inf')
            self.newroute[station] = []

        # Saves all the optimized routes
        self.prunedroutes = {}
        

    def map_shortest(self, starting_station):
        """Maps all nodes and finds the shortest route to all the nodes from the source node
           Saves these routes for usage of the move function"""
        # Saves queue for next steps
        queue = []
        visited = []
        counter = 0

        # Initializes correct values for the starting station
        self.distance_to[starting_station] = 0

        # Takes the source station and starts mapping outwards to find shortest paths to all possible
        current_station = self.oldroutes[starting_station]

        while True:
            counter += 1
            visited.append(current_station.name)
            tempkeys = current_station.connections.keys()

            # Queues station outward
            for station in tempkeys:
                if station not in visited:
                    if station not in queue:
                        queue.append(station)           

            # Checks if the route length from this path is better than the old length. If so change the route and the length
            for station in tempkeys:
                if station not in visited:
                    if current_station.connections[station] < self.distance_to[station]:
                        self.distance_to[station] = self.distance_to[current_station.name] + current_station.connections[station]
                        self.newroute[station] = self.newroute[current_station.name] + [current_station.name]

            if len(queue) > 0:
                newstat = queue.pop(0)
                current_station = self.oldroutes[newstat]
            
            if len(queue) == 0:
                break
            
        # Adds the starting/ending station to the route
        for key in self.newroute:
            self.newroute[key].append(key)

        # Writes new dictionary with the inefficient connections left out
        for station in self.newroute:       
            for i in range(0, len(self.newroute[station]) - 1, 1):
                stationname1 = self.newroute[station][i]
                stationname2 = self.newroute[station][i + 1]
                
                # If station 1 is in prunedroutes, simply add the second station as a connection
                if stationname1 in self.prunedroutes:
                    self.prunedroutes[stationname1].add_station(stationname2, self.oldroutes[stationname1].connections[stationname2])

                # If station 1 is not in prunedroutes, add the station as a station-class object and add the connection
                elif stationname1 not in self.prunedroutes:
                    self.prunedroutes[stationname1] = Station(stationname1)
                    self.prunedroutes[stationname1].add_station(stationname2, self.oldroutes[stationname1].connections[stationname2])

                # If station 2 is in prunedroutes, simply add the first station as a connection
                if stationname2 in self.prunedroutes:
                    self.prunedroutes[stationname2].add_station(stationname1, self.oldroutes[stationname2].connections[stationname1])

                # If station 2 is not in prunedroutes, add the station as a station-class object and add the connection
                elif stationname2 not in self.prunedroutes:
                    self.prunedroutes[stationname2] = Station(stationname2)
                    self.prunedroutes[stationname2].add_station(stationname1, self.oldroutes[stationname2].connections[stationname1])      
        

    def starting_station(self, station_dictionary, statnames):
        """Picks the starting station from a list of all possible stations
           Does this on the basis of the most connections"""
        # Ensures minimum spanning tree is only generated once
        if self.gencount == 0:
            self.oldroutes = station_dictionary
            for station in self.oldroutes:
                self.distance_to[station] = float('inf')
                self.newroute[station] = []
<<<<<<< HEAD
            # self.map_shortest('Utrecht Centraal')
=======
>>>>>>> 7299464bebceb37f79122b6fc6a3fb87a7f68534
            self.map_shortest(str(most_connection_start_heuristic(station_dictionary)))
            self.gencount += 1 
            
        return self.start_heuristic(self.prunedroutes)


    def move(self, current_station, train_stations, station_dictionary): 
        """Moves to the next station along the precalculated route of the dijkstra algorithm
           When destination is reached, removes the line from possible lines"""
        time = 0
        train_stations.append(current_station)

        # Resets every station in the pruned dictionary to unvisited after every run as this only generates once
        if current_station == None:
            for station in self.prunedroutes:
                temp_station = self.prunedroutes[station]
                for connection in temp_station.connection_visited:
                    temp_station.station_unvisit(str(connection))
            return train_stations, time

        while True:
            next_station = self.move_heuristic(current_station, train_stations, self.prunedroutes)
            if next_station is None:
                return train_stations, time

            # Keeps track of the time the trajectory takes
            all_time: int = time + current_station.connections.get(str(next_station))

              # stops if time is more than 3 hours
            if all_time > 180:
                return train_stations, time
            else:
                time: float = all_time

            # Sets connections to and from to visited
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))

            # Sets original station dictionary to visited to calculate the correct fraction
            station_dictionary[current_station.name].stationvisit(str(next_station))
            station_dictionary[next_station.name].stationvisit(str(current_station))

            current_station = next_station
            train_stations.append(current_station)