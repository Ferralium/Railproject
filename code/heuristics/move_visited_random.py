from station import Station
from typing import Optional
import random


def visited_random_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]) -> Optional[Station]:
    """Moves randomly to the next unused connection"""

    # Gets a random connection
    possible_next_station: str | Station = random.choice(list(curr.connections))
    next_station: Optional[Station] = stations.get(possible_next_station)

    check_stations: bool = all(station is True for station in curr.connection_visited.values())

    # If all connections are used, then a random connection is chosen
    if check_stations is True:
        possible_next_station = random.choice(list(curr.connections))
        next_station = stations.get(possible_next_station)
    # Random conection is chosen that has not been used yet
    else:
        while curr.is_visited(str(next_station)) is True:
            possible_next_station = random.choice(list(curr.connection_visited))
            next_station = stations.get(possible_next_station)

    return next_station