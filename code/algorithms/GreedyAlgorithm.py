from station import Station


class GreedyAlgorithm:
    """Algorithm for RailNL which picks stations with the least travel time and connections"""
    def __init__(self):
        pass


    def starting_station(self, station_dictionary, _):
        """Picks a starting station which has the least connections to move from outside to inside of connections"""
        first_number_connections = list(station_dictionary.values())[0]
        highest_unused_connections = first_number_connections.connection_count
        all_stations_true: int = 0

        # Goes through all stations in the dictionary to pick a suitable station
        for station in station_dictionary:
            check_connections: Station = station_dictionary.get(station)
            check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
            possible_current_station: Station = station_dictionary.get(str(check_connections))

            if check_startingpoint is True:
                all_stations_true += 1

            # Prioritises stations with only one conenction
            if check_connections.connection_count == 1:
                    if check_startingpoint is False:
                        current_station: Station = station_dictionary.get(str(possible_current_station))
                        break
            # Checks the station with the least connection 
            elif check_connections.connection_count != 1 or check_startingpoint == False:
                unused_connections: int = 0
                for connections in possible_current_station.connection_visited.values():
                    if connections == False:
                        unused_connections += 1
                if unused_connections < highest_unused_connections and unused_connections != 0:
                    highest_unused_connections = unused_connections
                    current_station = station_dictionary.get(str(possible_current_station))

        # Returns None if all connections have been visited
        if all_stations_true is len(station_dictionary):
            current_station = None

        return current_station


    def move(self, current_station, train_stations, stations_dictionary):
        """Moves to the next connection with the least travel time"""
        time = 0
        all_stations_true = 0
        
        # Adds current station to the list
        train_stations.append(current_station)

        if current_station == None:
            return train_stations, time

        while True:
            shortest_connection = 100
            check_stations: bool = all(station is True for station in current_station.connection_visited.values())

            # If all connections are used, the shortest one is chosen
            if check_stations is True:
                for station in stations_dictionary:
                    if all_stations_true == len(stations_dictionary):
                        return train_stations, time
                    else:
                        for connections in current_station.connections:
                            check_connections = stations_dictionary.get(connections)
                            for value in check_connections.connections.values():
                                if value < shortest_connection:
                                    shortest_connection = value
                                    next_station = stations_dictionary.get(connections)
            else:
                # The shortest connection that has not been used is chosen
                for connections in current_station.connections:
                    check_connections = stations_dictionary.get(connections)
                    if current_station.connections[connections] < shortest_connection and current_station.connection_visited[connections] is False:
                        shortest_connection = current_station.connections[connections]
                        next_station = stations_dictionary.get(connections)

            # Keeps track of the time the trajectory takes
            all_time: int = time + current_station.connections.get(str(next_station))

            # Stops if time is more than 3 hours
            if all_time > 180:
                return train_stations, time
            else:
                time = time + current_station.connections.get(str(next_station))

            # Sets the connection as visited
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))
            current_station = stations_dictionary.get(str(next_station))

            # Adds current station to the list
            train_stations.append(current_station)
