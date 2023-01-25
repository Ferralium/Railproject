import random
from station import Station


def least_connection_start_heuristic(stations: dict[str, Station]) -> Station:
    """Picks a starting station with the least connections"""
    first_number_connections = list(stations.values())[0]
    highest_unused_connections = first_number_connections.connection_count
    all_stations_true: int = 0

    for station in stations:
        check_connections: Station = stations.get(station)
        check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
        possible_current_station: Station = stations.get(str(check_connections))

        if check_startingpoint is True:
            all_stations_true += 1

        if check_connections.connection_count == 1:
                if check_startingpoint is False:
                    current_station: Station = stations.get(str(possible_current_station))
                    break
        elif check_connections.connection_count != 1 or check_startingpoint == False:
            unused_connections: int = 0
            for connections in possible_current_station.connection_visited.values():
                if connections == False:
                    unused_connections += 1
            if unused_connections < highest_unused_connections and unused_connections != 0:
                highest_unused_connections = unused_connections
                current_station = stations.get(str(possible_current_station))

    if all_stations_true is len(stations):
        starting_point: str = random.choice(list(stations.keys()))
        current_station = stations.get(starting_point)

    return current_station