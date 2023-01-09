class Station:
    def __init__(self, stationname):
        self.connections = {}
        self.name = stationname
        self.connectioncount = 0

    