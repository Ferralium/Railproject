import random
from station import Station


def random_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]) -> Station:
    """returns a random starting station"""
    return stations.get(random.choice(list(curr.connections.keys())))