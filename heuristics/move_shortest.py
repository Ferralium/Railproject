from station import Station


def shortest_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]):
    """Moves to the next connections with the least travel time"""

    #shortest_station = None
    #shortest_time = 0
    #previously_visited = True
    #for station_str in curr.connections:
    #    station = stations.get(station_str)
    #    if station not in visited:
    #        time = curr.connections.get(station_str)
    #        curr_previously_visited = station_str in curr.connection_visited
    #        if shortest_station is None:
    #            shortest_station = station
    #            shortest_time = time
    #            previously_visited = curr_previously_visited
    #        elif (not curr_previously_visited and previously_visited) or shortest_time > time:
    #            shortest_station = station
    #            shortest_time = time
    #            previously_visited = station_str in curr.connection_visited
    
    #return shortest_station

    shortest_connection = 100
    # print(f'hello {curr.connection_visited}')

    check_stations: bool = all(station is True for station in curr.connection_visited.values())
    if check_stations is True:
        for connections in curr.connections:
            check_connections = stations.get(connections)
            for value in check_connections.connections.values():
                if value < shortest_connection:
                    shortest_connection = value
                    next_station = stations.get(connections)
    else:
        for connections in curr.connections:
            check_connections = stations.get(connections)
            if curr.connections[connections] < shortest_connection and curr.connection_visited[connections] is False:
                shortest_connection = curr.connections[connections]
                next_station = stations.get(connections)

    return next_station