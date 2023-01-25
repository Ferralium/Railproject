import random
from station import Station

def random_start_heuristic(stations: dict[str, Station]):
    return random.choice(list(stations.values()))

def random_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]):
    return stations.get(random.choice(list(curr.connections.keys())))