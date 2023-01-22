import random
from station import Station

class LeastConnections:
    def __init__(self):
        pass

    def starting_station(self, station_dictionary, statnames):
        """Picks a starting station which has the least connections to move from outside to inside of connections"""
        first_number_connections = list(station_dictionary.values())[0]
        highest_unused_connections = first_number_connections.connection_count
        # highest_unused_connections = station_one.connection_count
        all_stations_true: int = 0

        for station in station_dictionary:
            print(station)
            check_connections: Station = station_dictionary.get(station)
            check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
            possible_current_station: Station = station_dictionary.get(str(check_connections))

            if check_startingpoint is True:
                all_stations_true += 1

            if check_connections.connection_count == 1:
                    if check_startingpoint is False:
                        current_station: Station = station_dictionary.get(str(possible_current_station))
                        break
            elif check_connections.connection_count != 1 or check_startingpoint == False:
                # possible_current_station = self.stations.get(str(check_connections))
                unused_connections: int = 0
                for connections in possible_current_station.connection_visited.values():
                    # print(connections)
                    if connections == False:
                        unused_connections += 1
                print(unused_connections)
                print(highest_unused_connections)
                if unused_connections < highest_unused_connections and unused_connections != 0:
                    highest_unused_connections = unused_connections
                    current_station = station_dictionary.get(str(possible_current_station))

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
        print(train_stations)
        # print(current_station.connection_visited.values())

        while True:
            print(current_station)

            check_used_connections: bool = all(station is True for station in current_station.connection_visited.values())

            # possible_next_stations = list(current_station.connections)
            # print(possible_next_stations)

            # if len(possible_next_stations) == 2 and check_used_connections != True:
            #     str_next_station = possible_next_stations[0]
            #     next_station = stations_dictionary.get(str(str_next_station))
            #     # amount_of_connections = len(next_station.connections)
            # else:
            # temp = stations_dictionary.get(possible_next_stations[0])
            # amount_of_connections = len(temp.connections)
            lowest_unused_connection = 100
            all_connections_used = 0

            for possible_station in current_station.connections:
                # print("q")
                counting_possible_station = stations_dictionary.get(possible_station)
                check_used_connections: bool = all(station is True for station in counting_possible_station.connection_visited.values())
                if check_used_connections is False:
                    # print("2")
                    
                    for connection in counting_possible_station.connection_visited:
                        unused_connection = 0
                        # print("3")
                        if connection is False:
                            unused_connection += 1
                    # if unused_connection < lowest_unused_connection:
                    if unused_connection < lowest_unused_connection and unused_connection != 1:
                        next_station = stations_dictionary.get(str(possible_station))
            
            # name_next_station: str = random.choice(list(current_station.connections))
            # next_station = stations_dictionary.get(name_next_station)
                    # all_connections_used += 0
            
            # if all_connections_used == len(current_station.connections):
            #     # print("4")
            #     name_next_station: str = random.choice(current_station.connections)
            #     next_station = stations_dictionary.get(name_next_station)


                    # also count the connectiosn that are False!!! those are the ones that count and as long they are not 0
                    # amount_of_connections_station = len(counting_possible_station.connections)
                    # if amount_of_connections_station < amount_of_connections:
                    #     amount_of_connections = amount_of_connections_station
                    #     next_station = stations_dictionary.get(str(possible_station))

            # print(f'hi {amount_of_connections}')
            print(next_station)
            print(f'c {current_station.connections.get(str(next_station))}')

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
            current_station: Station = stations_dictionary.get(str(next_station))

            # voeg current_station toe aan de lijst
            train_stations.append(current_station)


            # # WERKT NIET, OM HEM OP VISITED TE ZETTEN


            # # print(f' Current Station: {current_station}')
            # # check_startingpoint: bool = all(station is True for station in current_station.connection_visited.values())
            # # print(check_startingpoint)
            # print(f'1: {next_station}')
            # print(f'1: {current_station}')
            # print(current_station.connection_visited.values())
            # current_station.stationvisit(str(next_station))
            # # print(current_station.connection_visited.values())
            # next_station.stationvisit(str(current_station))
            # # print(current_station.stationvisit(str(next_station)))
            # # print(next_station.stationvisit(str(current_station)))
            # current_station: Station = stations_dictionary.get(str(next_station))
            # print(current_station.connection_visited.values())

            # # voeg current_station toe aan de lijst
            # train_stations.append(current_station)
            # # print("treinstation toegevoegd")

            print(f' Next Station: {current_station}')
            print(time)
            print(" ")


