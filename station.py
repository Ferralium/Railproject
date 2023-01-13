# underscores bij variabele namen als het meer dan 1 woord is?
class Station:
    def __init__(self, station_name):
        self.connections = {}
        self.connection_visited = {}
        self.name = station_name
        self.connection_count = 0

    def add_station(self, connection, distance):
        self.connections[connection] = distance
        self.connection_count += 1
        self.connection_visited[connection] = False

    def stationvisit(self, connection):
        self.connection_visited[connection] = True
    
    def is_visited(self, next_connection):
        return self.connection_visited[next_connection]
    
    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'