import random 

class MostConnectionsHeuristic:

    def __init__(self):
        pass

    def starting_station(self, station_dictionary, statnames):
        highest_unused_connections = 0
        all_stations_true = 0

        for station in station_dictionary:
            # print(station)
            check_connections: Station = station_dictionary.get(station)
            check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
            possible_current_station: Station = station_dictionary.get(str(check_connections))

            if check_startingpoint is True:
                all_stations_true += 1
            else:
                unused_connections: int = 0
                for connections in possible_current_station.connection_visited.values():
                    if connections == False:
                        unused_connections += 1
                    print(station, connections, unused_connections)

                if unused_connections > highest_unused_connections:
                    highest_unused_connections = unused_connections
                    current_station = station_dictionary.get(str(stations))

        print(len(station_dictionary))
        print(all_stations_true)
        if all_stations_true is len(station_dictionary):
            starting_point: str = random.choice(statnames)
            current_station = station_dictionary.get(starting_point)

        return current_station

    def move(self, current_station, train_stations, stations_dictionary):
        time = 0
        

        # voeg de current station toe aan de lijst
        train_stations.append(current_station)
        # print(train_stations)

        while True:
            highest_unused_connections = 0

            check_stations: bool = all(station is True for station in current_station.connection_visited.values())
            
            # alle trajecten bereden? kies dan random...
            if check_stations is True:
                possible_next_station = random.choice(list(current_station.connections))
                next_station = stations_dictionary.get(possible_next_station)
                print("hi")
            else:
                print("bye")
                for connections in current_station.connections:
                    print(connections)
                    possible_next_station = stations_dictionary.get(connections)
                    for station in possible_next_station.connection_visited.values():
                        unused_connection = 0
                        print(possible_next_station.connection_visited, station)
                        if station is False:
                            unused_connection += 1
                    print(highest_unused_connections)
                    print(unused_connection)
                    print(station)
                    # gaat hier fout, na den haag HS
                    if unused_connection > highest_unused_connections:
                        highest_unused_connections = unused_connection
                        print("lol")
                        next_station = stations_dictionary.get(connections)
                        print(next_station)
            print("c")

            all_time: int = time + current_station.connections.get(str(next_station))

            # stops if time is more than 3 hours
            if all_time > 180:
                print(f'hi {all_time}')
                print(f'this will be returned {time}')
                return train_stations, time
            else:
                time = time + current_station.connections.get(str(next_station))

            print(f' Current Station: {current_station}')
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))

            current_station = stations_dictionary.get(str(next_station))

            # voeg current_station toe aan de lijst
            train_stations.append(current_station)

            print(f' Next Station: {current_station}')
            print(time)
            print(" ")
