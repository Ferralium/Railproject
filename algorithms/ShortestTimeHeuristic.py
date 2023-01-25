import random 


class ShortestTimeHeuristic:

    def __init__(self):
        pass

    def starting_station(self, station_dictionary, statnames):
        """"Picks a purely random starting station from the list of all possible stations"""
        # print(station_dictionary.values())
        # print(station_dictionary.keys())
        current_station = random.choice(list(station_dictionary.values()))
        return current_station
        # shortest_connection = 100
        # all_stations_true = 0

        # for station in station_dictionary:
        #     check_connections = station_dictionary.get(station)
        #     check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
        #     print(check_startingpoint)
        #     if check_startingpoint is True:
        #         all_stations_true += 1
        #     else:
        #         for possible_station in check_connections.connection_visited:
        #             print(station)
        #             if check_connections.connections[possible_station] < shortest_connection and check_connections.connection_visited[possible_station] is False:
        #                 shortest_connection = check_connections.connections[possible_station]
        #                 current_station = check_connections
        #                 print("v")
        #                 print(shortest_connection)
        #                 print(f' Current Station: {current_station}')


        # if all_stations_true is len(station_dictionary):
        #     starting_point: str = random.choice(statnames)
        #     current_station = station_dictionary.get(starting_point)
        
        # return current_station

    def move(self, current_station, train_stations, stations_dictionary):
        pass
        time = 0
        all_stations_true = 0
        
        # voeg de current station toe aan de lijst
        train_stations.append(current_station)
        print(current_station)

        while True:
            
            shortest_connection = 100
            print(f'hello {current_station.connection_visited}')

            check_stations: bool = all(station is True for station in current_station.connection_visited.values())
        
            if check_stations is True:
                for station in stations_dictionary:
                    if all_stations_true == len(stations_dictionary):
                        return train_stations, time
                    else:
                        for connections in current_station.connections:
                            check_connections = stations_dictionary.get(connections)
                            # print(check_connections)
                            for value in check_connections.connections.values():
                                if value < shortest_connection:
                                    shortest_connection = value
                                    # print(check_connections)
                                    chance = random.uniform(0,10)
                                    if chance < 7:
                                        next_station = stations_dictionary.get(connections)
                                    else:
                                        possible_next_station = random.choice(list(current_station.connections.keys()))
                                        next_station = stations_dictionary.get(str(possible_next_station))
            else:
                for connections in current_station.connections:
                    check_connections = stations_dictionary.get(connections)
                    
                    if current_station.connections[connections] < shortest_connection and current_station.connection_visited[connections] is False:
                  
                        shortest_connection = current_station.connections[connections]
                        chance = random.uniform(0,10)
                        print(chance)
                        if chance < 7:
                            next_station = next_station = stations_dictionary.get(connections)
                        else:
                            possible_next_station = random.choice(list(current_station.connections.keys()))
                            next_station = stations_dictionary.get(str(possible_next_station))
                            


            all_time: int = time + current_station.connections.get(str(next_station))
           

            # stops if time is more than 3 hours
            if all_time > 180:
                print(f'hi {all_time}')
                print(f'this will be returned {time}')
                return train_stations, time
            else:
                time = time + current_station.connections.get(str(next_station))
                print(f'current {time}')

            print(f' Current Station: {current_station}')
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))
            current_station = stations_dictionary.get(str(next_station))
            print(current_station.connection_visited)

            # voeg current_station toe aan de lijst
            train_stations.append(current_station)
          

            print(f' Next Station: {current_station}')
            print(time)
            print(" ")

