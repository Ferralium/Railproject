class Station:
    """Creates a station object"""
    def __init__(self, station_name: str) -> None:
        """creates a dictionary with all the connections from the Station,
        creates a dictionary that track which conenctions are used,
        counts all the connections """
        self.connections: dict[str, int]= {}
        self.connection_visited: dict[str, bool] = {}
        self.name: str = station_name
        self.connection_count: int = 0
        self.visits_counter: dict[str, int] = {}

    def add_station(self, connection: str, distance: int) -> None:
        """adds a station to the connections dictionary"""
        self.connections[connection] = distance
        self.connection_count += 1
        self.connection_visited[connection] = False
        self.visits_counter[connection] = 0

    def stationvisit(self, connection: str) -> None:
        """sets a connections to visited"""
        self.connection_visited[connection] = True
        self.visits_counter[connection] += 1

    def station_unvisit(self, connection: str) -> None:
        self.connection_visited[connection] = False
        self.visits_counter[connection] -= 1

    def is_visited(self, next_connection: str) -> bool:
        """checks if a connection is visited and return True or False"""
        return self.connection_visited[next_connection]

    def check_number_visits(self, connection: str) -> int:
        """ Checks how many times the connection has been visited """
        return self.visits_counter[connection]

    def one_less_visit(self, connection: str) -> None:
        """ lowers the number of visits by 1 """
        self.visits_counter[connection] -= 1

    def __str__(self) -> str:
        """returns the station as a string"""
        return f'{self.name}'

    def __repr__(self) -> str:
        """returns the station as a string"""
        return f'{self.name}'
