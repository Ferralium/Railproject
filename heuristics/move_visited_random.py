from station import Station
import random


def visited_random_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]):
    """Moves randomly to next not-visited connection"""

    possible_next_station: str | Station = random.choice(list(curr.connections))
    next_station: Station = stations.get(possible_next_station)

    check_stations: bool = all(station is True for station in curr.connection_visited.values())

    if check_stations is True:
        possible_next_station = random.choice(list(curr.connections))
        next_station = stations.get(possible_next_station)
    else:
        while curr.is_visited(str(next_station)) is True:
            possible_next_station = random.choice(list(curr.connection_visited))
            next_station = stations.get(possible_next_station)

    return next_station