class Station:
    def __init__(self, stationname):
        self.connections = {}
        self.name = stationname
        self.connectioncount = 0
        self.isvisited = False

    def add_station(self, connection, distance):
        self.connections[connection] = distance
        self.connectioncount += 1

    def stationvisit(self):
        self.isvisited = True