"""
    railsolver.py

    Door:
        Chiara Schut - 
        Berber Siersma - 
        Jeroen Steenhof - 12709425
    Minor Programmeren - Algoritmen en Heuristieken

    Attempts to solve heuristic problem with train stations.
"""

from station import Station

class Railsolver():
    def __init__(self):
        self.stations = {}

    def load_stations(self):
    # Load functie om alles van de CSV in te laden
        with open('data/ConnectiesHollandKlein.csv') as f:
            next(f)
            for line in f:
                templine = line
                templine = templine.strip().split(',')
                if templine[0] in self.stations:
                    # Hier functie aanroepen uit station om connectie toe te voegen met de lengte als value
                    self.stations[templine[0]].add_station(templine[1], templine[2])

                elif templine[0] not in self.stations:
                    # Hier functie die nieuwe station aanmaakt en de connectie gelijk toevoegt
                    self.stations[templine[0]] = Station(templine[0])
                    self.stations[templine[0]].add_station(templine[1], templine[2])        
                
                # Hier tweede functie die checkt of destination station ook al bestaat, zo niet voegt deze toe
                if templine[1] not in self.stations:
                    self.stations[templine[1]] = Station(templine[1])
                    self.stations[templine[1]].add_station(templine[0], templine[2])

if __name__ == '__main__':
    wisselstoring = Railsolver()
    wisselstoring.load_stations()