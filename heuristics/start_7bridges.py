from station import Station
import random

def sevenbridges_start_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]):
    """Chooses stating station with uneven number of unused connections,
    based on the 7 bridges problem"""

    while True:
        current_station = random.choice(list(stations.values()))
        ununsed_connection = 0

        for unvisited_connection in current_station.connection_visited.values():
            if unvisited_connection is False:
                ununsed_connection += 0

        if not ununsed_connection % 2 is 0:
            break

    return current_station