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
    with open('data/stations') as f:
