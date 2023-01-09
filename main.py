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
    
    # Initializes the stations dictionary for the railsolver
    def __init__(self):
        self.stations = {}

    def load_stations(self):
        """Loads the stations with distances from the CSV.
           Also creates new stations for the connections if they are not already in the dict"""
    
        with open('data/ConnectiesHollandKlein.csv') as f:
            # Met de next functie wordt de eerste lijn overgeslagen, dit geeft alleen informatie over de inhoud
            next(f)

            # For loop iterates over the lines in the csv and modifies them to usable format
            for line in f:
                templine = line
                templine = templine.strip().split(',')

                # For loop schrijven die voor zowel source als destination station inlaadt en zo beide connecties toevoegd
                # Belangrijk is voor beide de check of station al bestaat of niet, daarom for loop

                # Checks if station already exists, if so adds connection
                if templine[0] in self.stations:
                    self.stations[templine[0]].add_station(templine[1], templine[2])

                # If the station does not exist initializes the station and adds the connection
                elif templine[0] not in self.stations:
                    self.stations[templine[0]] = Station(templine[0])
                    self.stations[templine[0]].add_station(templine[1], templine[2])

                # Checks whether the connection already exists in the stations and adds it if this is not the case
                if templine[1] not in self.stations:
                    self.stations[templine[1]] = Station(templine[1])
                    self.stations[templine[1]].add_station(templine[0], templine[2])        
                
                

if __name__ == '__main__':
    wisselstoring = Railsolver()
    wisselstoring.load_stations()