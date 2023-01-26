from station import Station
import random


def visited_random_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]) -> Station:
    """Moves randomly to the next unused connection"""

    possible_next_station: str | Station = random.choice(list(curr.connections))
    next_station: Station = stations.get(possible_next_station)

    check_stations: bool = all(station is True for station in curr.connection_visited.values())

    # if connections are used, then a random connection is chosen
    if check_stations is True:
        possible_next_station: Station = random.choice(list(curr.connections))
        next_station: Station = stations.get(possible_next_station)
    # random unused conection is chosen
    else:
        while curr.is_visited(str(next_station)) is True:
            possible_next_station: Station = random.choice(list(curr.connection_visited))
            next_station: Station = stations.get(possible_next_station)

    return next_station