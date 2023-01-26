from typing import Callable
from algorithm import Algorithm
from station import Station


class HeuristicAlgorithm(Algorithm):
    """Creates an Algorithm that can call and use different heuritics"""
    def __init__(self, start_heuristic: Callable[[dict[str, Station]], Station], move_heuristic: Callable[[Station, list[Station], dict[str, Station]], Station]) -> None:
        """Object has a start heuristic and a move heuristic"""
        self.start_heuristic: Callable[[dict[str, Station]], Station] = start_heuristic
        self.move_heuristic: Callable[[Station, list[Station], dict[str, Station]]] = move_heuristic

    def starting_station(self, station_dictionary: dict[str, Station], _) -> Station:
        """returns the starting station chosen by the start_heuristic"""
        return self.start_heuristic(station_dictionary)
    
    def move(self, current_station: Station, train_stations: list[Station], station_dictionary: dict[str, Station]) -> None:
        """Moves to the next connections based on the move_heuristic"""

        time: float = 0
        train_stations.append(current_station)

        if current_station == None:
            return train_stations, time

        # one loop is a move from station A to station B
        while True:
            next_station: Station = self.move_heuristic(current_station, train_stations, station_dictionary)
            if next_station is None:
                return train_stations, time

            # keeps track of the time the trajectory takes
            all_time: int = time + current_station.connections.get(str(next_station))

            # stops if time is more than 3 hours
            if all_time > 180:
                return train_stations, time
            else:
                time: float = all_time

            # sets connections to and from to visited
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))

            current_station = next_station
            train_stations.append(current_station)