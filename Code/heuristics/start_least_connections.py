from station import Station
from typing import Optional


def least_connection_start_heuristic(stations: dict[str, Station]) -> Optional[Station]:
    """Picks a starting station with the least unused connections"""
    first_number_connections = list(stations.values())[0]
    highest_unused_connections = first_number_connections.connection_count
    all_stations_true: int = 0

    # loops over all stations
    for station in stations:
        check_connections: Optional[Station] = stations.get(station)
        check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
        possible_current_station: Optional[Station] = stations.get(str(check_connections))

        # counts stations that have used all connections
        if check_startingpoint is True:
            all_stations_true += 1

        # checks if station has 1 unused connection
        if check_connections.connection_count == 1 and check_startingpoint == False:
                current_station: Optional[Station] = stations.get(str(possible_current_station))
                break
        # checks number of unused connections
        elif check_connections.connection_count != 1 or check_startingpoint == False:
            unused_connections: int = 0
            for connections in possible_current_station.connection_visited.values():
                if connections == False:
                    unused_connections += 1
            # sets station as current station if it has the lowest number of unused connections
            if unused_connections < highest_unused_connections and unused_connections != 0:
                highest_unused_connections = unused_connections
                current_station = stations.get(str(possible_current_station))

    # returns None if all connections have been visited
    if all_stations_true is len(stations):
        current_station = None
 
    return current_station