from station import Station
import random

def sevenbridges_start_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]):

    current_station = random.choice(list(stations.values()))

    while current_station.connection_count % 2 is 0:
        current_station = random.choice(list(stations.values()))

    return current_station