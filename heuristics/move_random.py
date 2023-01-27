import random
from typing import Optional
from station import Station


def random_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]) -> Optional[Station]:
    """returns a random starting station"""
    return stations.get(random.choice(list(curr.connections.keys())))