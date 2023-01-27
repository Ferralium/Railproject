import random
from station import Station


def least_connection_start_heuristic(stations: dict[str, Station]) -> Station:
    """Picks a starting station with the least unused connections"""
    first_number_connections = list(stations.values())[0]
    highest_unused_connections = first_number_connections.connection_count
    all_stations_true: int = 0

    # loops over all stations
    for station in stations:
        check_connections: Station = stations.get(station)
        check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
        possible_current_station: Station = stations.get(str(check_connections))

        # counts stations that have used all connections
        if check_startingpoint is True:
            all_stations_true += 1

        # checks if station has 1 unused connection
        if check_connections.connection_count == 1 and check_startingpoint == False:
                current_station: Station = stations.get(str(possible_current_station))
                break
        # checks number of unused connections
        elif check_connections.connection_count != 1 or check_startingpoint == False:
            unused_connections: int = 0
            for connections in possible_current_station.connection_visited.values():
                if connections == False:
                    unused_connections += 1
            if unused_connections < highest_unused_connections and unused_connections != 0:
                highest_unused_connections = unused_connections
                current_station = stations.get(str(possible_current_station))

    # if all connections are used, a random starting station is chosen
    if all_stations_true is len(stations):
        current_station = None
 
    return current_station