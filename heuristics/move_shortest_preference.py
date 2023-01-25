from station import Station
import random

def shortest_move_heuristic(curr: Station, visited: list[Station], stations: dict[str, Station]):
    """Preference for moving to the next connection that has not been visited yet and has the least travel time"""

    shortest_connection = 100
    print(f'hello {curr.connection_visited}')

    check_stations: bool = all(station is True for station in curr.connection_visited.values())

    if check_stations is True:
        for station in stations:
            # if all_stations_true == len(stations_dictionary):
            #     return train_stations, time
            # else:
            for connections in curr.connections:
                check_connections = stations.get(connections)
                # print(check_connections)
                for value in check_connections.connections.values():
                    if value < shortest_connection:
                        shortest_connection = value
                        # print(check_connections)
                        chance = random.uniform(0,10)
                        if chance < 7:
                            next_station = stations.get(connections)
                        else:
                            possible_next_station = random.choice(list(curr.connections.keys()))
                            next_station = stations.get(str(possible_next_station))
    else:
        for connections in curr.connections:
            check_connections = stations.get(connections)
            
            if curr.connections[connections] < shortest_connection and curr.connection_visited[connections] is False:
            
                shortest_connection = curr.connections[connections]
                chance = random.uniform(0,10)
                print(chance)
                if chance < 7:
                    next_station = next_station = stations.get(connections)
                else:
                    possible_next_station = random.choice(list(curr.connections.keys()))
                    next_station = stations.get(str(possible_next_station))


    return next_station