import random
from station import Station
from typing import Optional


def most_connection_start_heuristic(stations: dict[str, Station]) -> Optional[Station]:
    """Chooses a starting station with the most unused connections"""
    highest_unused_connections = 0
    all_stations_true = 0

    # loops over all stations
    for station in stations:
        check_connections: Optional[Station] = stations.get(station)
        check_startingpoint: bool = all(station is True for station in check_connections.connection_visited.values())
        possible_current_station: Optional[Station] = stations.get(str(check_connections))

        # counts stations that have used all connections
        if check_startingpoint is True:
            all_stations_true += 1
        else:
            # counts number of unused connections of a station
            unused_connections: int = 0
            for connections in possible_current_station.connection_visited.values():
                if connections == False:
                    unused_connections += 1
            # sets station as current station if the station has the highest number of unused connections
            if unused_connections > highest_unused_connections:
                highest_unused_connections = unused_connections
                current_station = stations.get(str(station))

    # returns None if all connections have been visited
    if all_stations_true is len(stations):
        current_station = None
    
    return current_station
