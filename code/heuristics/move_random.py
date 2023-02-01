import random
from typing import Optional
from station import Station


def random_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]) -> Optional[Station]:
    """Chooses and returns a random station the train will move to"""
    return stations.get(random.choice(list(curr.connections.keys())))