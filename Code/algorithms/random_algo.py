import random

from station import Station

class RandomAlgorithm:
    """Algorithm for RailNL which picks stations and connections randomly"""
    def __init__(self):
        pass

    def starting_station(self, station_dictionary, statnames):
        """"Picks a purely random starting station from the list of all possible stations"""
        current_station = random.choice(list(station_dictionary.values()))
        return current_station

    def move(self, current_station, train_stations, stations_dictionary):
        time = 0

        # Adds the current station to the list
        train_stations.append(current_station)

        while True:

            # Moves to next random connection that has not been visited yet
            possible_next_station: Station = random.choice(list(current_station.connections.keys()))
            next_station: Station = stations_dictionary.get(possible_next_station)


            all_time: int = time + current_station.connections.get(str(next_station))

            # Stops if time is more than 3 hours
            if all_time > 180:
                return train_stations, time
            else:
                time = time + current_station.connections.get(str(next_station))

            # Sets the connections to and from as visited
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))
            current_station: Station = stations_dictionary.get(str(next_station))

            # Adds current station to the list
            train_stations.append(current_station)