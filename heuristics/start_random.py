import random
from station import Station


def random_start_heuristic(stations: dict[str, Station]) -> Station:
    """randomly chooses and returns the starting station"""
    return random.choice(list(stations.values()))