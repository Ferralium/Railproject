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

    def add_station(self, connection: str, distance: int) -> None:
        """adds a station to the connections dictionary"""
        self.connections[connection] = distance
        self.connection_count += 1
        self.connection_visited[connection] = False

    def stationvisit(self, connection: str) -> None:
        """sets a connections to visited"""
        self.connection_visited[connection] = True
    
    def station_unvisit(self, connection) -> None:
        self.connection_visited[connection] = False
    
    def is_visited(self, next_connection: str) -> bool:
        """checks if a connection is visited and return True or False"""
        return self.connection_visited[next_connection]
    
    def __str__(self) -> str:
        """returns the station as a string"""
        return f'{self.name}'

    def __repr__(self) -> str:
        """returns the station as a string"""
        return f'{self.name}'