import random

class SmartAlgorithm:
    def __init__(self):
        pass

    def starting_station(self, station_dictionary):
        """"Picks a starting station which has the least connections to move from outside to inside of connections"""
        first_number_connections = list(self.stations.values())[0]
        highest_unused_connections = first_number_connections.connection_count
        # highest_unused_connections = station_one.connection_count
        all_stations_true: int = 0

        for station in self.stations:
            print(station)
            check_connections: Station = self.stations.get(station)
            check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
            possible_current_station: Station = self.stations.get(str(check_connections))

            if check_startingpoint is True:
                all_stations_true += 1

            if check_connections.connection_count == 1:
                    if check_startingpoint is False:
                        current_station: Station = self.stations.get(str(possible_current_station))
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
                    current_station = self.stations.get(str(possible_current_station))

        print(len(self.stations))
        print(all_stations_true)
        if all_stations_true is len(self.stations):
            starting_point: str = random.choice(self.statnames)
            current_station = self.stations.get(starting_point)

        return current_station

    def move(self, current_station, train_stations, stations_dictionary):
        time = 0

        # voeg de current station toe aan de lijst
        train_stations.append(current_station)
        print(train_stations)

        while True:

            # Moves to next random connection that has not been visited yet
            possible_next_station: str | Station = random.choice(list(current_station.connections))
            next_station: Station = self.stations.get(possible_next_station)

            check_stations: bool = all(station is True for station in current_station.connection_visited.values())

            if check_stations is True:
                possible_next_station = random.choice(list(current_station.connections))
                next_station = self.stations.get(possible_next_station)
            else:
                while current_station.is_visited(str(next_station)) is True:
                    possible_next_station = random.choice(list(current_station.connection_visited))
                    next_station = self.stations.get(possible_next_station)

            all_time: int = time + current_station.connections.get(str(next_station))

            # stops if time is more than 3 hours
            if all_time > 180:
                print(f'hi {all_time}')
                print(f'this will be returned {time}')
                return train_stations, time
            else:
                time = time + current_station.connections.get(str(next_station))

            print(f' Current Station: {current_station}')
            check_startingpoint: bool = all(station is True for station in current_station.connection_visited.values())
            print(check_startingpoint)
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))
            current_station: Station = self.stations.get(str(next_station))

            # voeg current_station toe aan de lijst
            train_stations.append(current_station)
            # print("treinstation toegevoegd")

            print(f' Next Station: {current_station}')
            print(time)
            print(" ")