from station import Station
import random


def sevenbridges_start_heuristic(stations: dict[str, Station]) -> Station:
    """Chooses starting station with uneven number of unused connections,
    based on the 7 bridges problem"""
    stations_visited: dict[Station, bool] = {}
    stations_even: dict[Station, bool] = {}

    while True:
        current_station = random.choice(list(stations.values()))
        check_startingpoint: bool = all(station is True for station in current_station.connection_visited.values())
        ununsed_connection = 0
        
        # sets connection to visited
        if check_startingpoint is True:
            stations_visited[current_station] = True
            stations_even[current_station] = True
        else: 
            # chooses random station and counts its unused conenctions
            for unvisited_connection in current_station.connection_visited.values():
                if unvisited_connection is False:
                    ununsed_connection += 1
            
            # checks if the amount of unused connection is uneven
            if ununsed_connection % 2 != 0:
                break
            else:
                stations_even[current_station] = True
        
        # returns None if all connections have been visited
        if len(stations_visited) is len(stations):
            current_station = None 
            break 
        # if all connections are used or only stations with an even number of connections are left, choose a random uneven station
        elif len(stations_even) is len(stations):
            while True:
                current_station = random.choice(list(stations.values()))
                if current_station.connection_count % 2 != 0:
                    break
            break

    return current_station

