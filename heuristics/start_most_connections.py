import random
from station import Station


def most_connection_start_heuristic(stations: dict[str, Station]) -> Station:
    highest_unused_connections = 0
    all_stations_true = 0

    for station in stations:
        check_connections: Station = stations.get(station)
        check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
        possible_current_station: Station = stations.get(str(check_connections))

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
                current_station = stations.get(str(stations))

    if all_stations_true is len(stations):
        starting_point: str = random.choice(list(stations.keys()))
        current_station = stations.get(starting_point)

    return current_station
