# underscores bij variabele namen als het meer dan 1 woord is?
class Station:
    def __init__(self, stationname):
        self.connections = {}
        self.connection_visited = {}
        self.name = stationname
        self.connectioncount = 0

    def add_station(self, connection, distance):
        self.connections[connection] = distance
        self.connectioncount += 1
        self.connection_visited[connection] = False

    def stationvisit(self, connection):
        self.connection_visited[connection] = True