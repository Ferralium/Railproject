from station import Station



class DijkstraAlgorithm:
    def __init__(self):
        """Dijkstra Algorithm aims to create a minimum spanning tree with the lowest cost distances
           to all points in the map from a single source station"""
        # Keeps the old dictionary with all the routes for safekeeping
        self.oldroutes = {}

        with open('data/ConnectiesNationaal.csv') as f:
            # Met de next functie wordt de eerste lijn overgeslagen, dit geeft alleen informatie over de inhoud
            next(f) 
            # For loop iterates over the lines in the csv and modifies them to usable format
            for line in f:
                templine: str = line

                # ik denk dat we deze een andere variabele naam moeten geven, anders werkt de typehint niet.
                templine = templine.strip().split(',')     

                # Checks if station already exists, if so adds connection
                if templine[0] in self.oldroutes:
                    self.oldroutes[templine[0]].add_station(templine[1], float(templine[2]))    

                # If the station does not exist initializes the station and adds the connection
                elif templine[0] not in self.oldroutes:
                    self.oldroutes[templine[0]] = Station(templine[0])
                    self.oldroutes[templine[0]].add_station(templine[1], float(templine[2]))   

                # Checks whether the connection already exists in the stations and adds it if this is not the case
                if templine[1] not in self.oldroutes:
                    self.oldroutes[templine[1]] = Station(templine[1])
                    self.oldroutes[templine[1]].add_station(templine[0], float(templine[2]))    
                elif templine[1] in self.oldroutes:
                    self.oldroutes[templine[1]].add_station(templine[0], float(templine[2]))

        self.newroute = {}
        self.distance_to = {}
        # self.unvisited = []

        # These are the variables required to to keep updating the MST
        for station in self.oldroutes:
            # self.unvisited.append(station)
            self.distance_to[station] = float('inf')
            self.newroute[station] = []

        # Saves all the optimized routes
        self.prunedroutes = {}
        
        pass

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

        while len(visited) < len(self.oldroutes):
            tempkeys = current_station.connections.keys()
            self.newroute[current_station.name].append(current_station.name)

            # If station has not been visited yet, add to the queue to visit
            for station in tempkeys:
                if station not in visited:
                    if station not in queue:
                        queue.append(station)

            # Checks if the route length from this path is better than the old length. If so change the route and the length
            for station in tempkeys:
                if current_station.connections[station] not in visited:
                    if current_station.connections[station] < self.distance_to[station]:
                        self.distance_to[station] = self.distance_to[current_station.name] + current_station.connections[station]
                        self.newroute[station] = self.newroute[current_station.name]

            counter += 1
            visited.append(current_station.name)
            if len(queue) > 0:
                newstat = queue.pop(0)
                current_station = self.oldroutes[newstat]

            if counter == 2:
                break
            
        # print(self.distance_to)
        print(self.newroute['Amsterdam Centraal'])

    def starting_station(self, station_dictionary, statnames):
        """Picks the starting station from a list of all possible stations
           Does this on the basis of the most connections"""
        # Function to pick the starting station
        starting_station = 0
        self.oldroutes = station_dictionary
        for station in station_dictionary:
            self.distance_to[station] = float('inf')
        self.map_shortest(station_dictionary, statnames)
        pass  

    def move(self): 
        """Moves to the next station along the precalculated route of the dijkstra algorithm
           When destination is reached, removes the line from possible lines"""
        pass

dijk = DijkstraAlgorithm()

# Check for updated distances
# print(dijk.distance_to)
dijk.map_shortest('Amsterdam Centraal')