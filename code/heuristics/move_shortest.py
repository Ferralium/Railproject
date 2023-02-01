from station import Station
from typing import Optional


def shortest_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]) -> Optional[Station]:
    """Moves to the next unused connection with the least travel time"""
    shortest_connection: int = 100
    check_stations: bool = all(station is True for station in curr.connection_visited.values())

    # If all connections are used, the shortest one is chosen
    if check_stations is True:
        for connections in curr.connections:
            check_connections: Optional[Station] = stations.get(connections)
            for value in check_connections.connections.values():
                if value < shortest_connection:
                    shortest_connection = value
                    next_station: Optional[Station] = stations.get(connections)
    else:
        # The shortest connection that has not been used is chosen
        for connections in curr.connections:
            check_connections = stations.get(connections)
            if curr.connections[connections] < shortest_connection and curr.connection_visited[connections] is False:
                shortest_connection = curr.connections[connections]
                next_station = stations.get(connections)

    return next_station