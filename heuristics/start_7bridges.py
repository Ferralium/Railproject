from station import Station
import random

def sevenbridges_start_heuristic(stations: dict[str, Station]):
    """Chooses stating station with uneven number of unused connections,
    based on the 7 bridges problem"""

    stations_visited = {}
    stations_even = {}

    while True:
        current_station = random.choice(list(stations.values()))
        check_startingpoint: bool = all(station is True for station in current_station.connection_visited.values())
        ununsed_connection = 0
        
        print(current_station)

        if check_startingpoint is True:
            print("hi")
            stations_visited[current_station] = True
            stations_even[current_station] = True
        else: 
            for unvisited_connection in current_station.connection_visited.values():
                print(unvisited_connection)
                if unvisited_connection is False:
                    ununsed_connection += 1
                    
            if ununsed_connection % 2 != 0:
                break
            else:
                stations_even[current_station] = True
        
        if len(stations_visited) is len(stations) or len(stations_even) is len(stations):
            while True:
                current_station = random.choice(list(stations.values()))
                if current_station.connection_count % 2 != 0:
                    break
            break

    return current_station

