import random

class RandomAlgorithm:
    def __init__(self):
        pass

    def starting_station(self, station_dictionary):
        """"Picks a purely random starting station from the list of all possible stations"""
        current_station = random.choice(list(station_dictionary.values()))
        print(f'random starting station: {current_station}')
        return current_station

    def move(self, current_station, train_stations, stations_dictionary):
        time = 0

        # voeg de current station toe aan de lijst
        train_stations.append(current_station)
        print(train_stations)

        while True:

            # Moves to next random connection that has not been visited yet
            possible_next_station: str | Station = random.choice(list(current_station.connections))
            next_station: Station = stations_dictionary.get(possible_next_station)


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
            current_station: Station = stations_dictionary.get(str(next_station))

            # voeg current_station toe aan de lijst
            train_stations.append(current_station)

            print(f' Next Station: {current_station}')
            print(time)
            print(" ")