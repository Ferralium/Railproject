import random
from station import Station

def random_start_heuristic(stations: dict[str, Station]):
    return random.choice(list(stations.values()))