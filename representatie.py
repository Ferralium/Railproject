from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import random

# Rework data to useable format

class Mapdrawer():
    def __init__(self):
        """Initializes the mapdrawer, loads in the correct coordinates from the csv"""

        # Remembers color combinations for use in random color generator
        self.colormap = []

        # Initializes the map projection with the Basemap module
        self.m = Basemap(projection = 'mill', llcrnrlat = 50.730, llcrnrlon = 3.279, urcrnrlat = 53.491, urcrnrlon = 7.295, resolution = 'h')

        # Extracts correct coordinates from the CSV. Maps these to the station name as key
        self.correctcoords = {}
        with open("data/StationsNationaal.csv") as f:
            next(f)
            for line in f:
                tempcoords = []
                templine = line.strip().split(',')
                xpt, ypt = self.m(float(templine[2]), float(templine[1]))
                tempcoords.append(xpt)
                tempcoords.append(ypt)

                self.correctcoords[templine[0]] = tempcoords

        # Extracts the connections between the stations into a list
        self.connections = []
        with open('data/ConnectiesNationaal.csv') as c:
            next(c)
            for line in c:
                tempconnect = []
                templine = line.strip().split(',')
                tempconnect.append(templine[0])
                tempconnect.append(templine[1])
                self.connections.append(tempconnect)
            
    def print_to_image(self):
        """Prints all the stations on a map made with Miller Cylindrical projection and saves the map as .PNG"""
        # Miller cylindrical projection
        self.m.drawcoastlines()
        self.m.drawcountries(linewidth=1)
        self.m.fillcontinents(color = 'coral', lake_color = 'aqua')

        # Drawing points on the map
        for station in self.correctcoords:
            self.m.plot(self.correctcoords[station][0], self.correctcoords[station][1], '.', markersize = 10, color = 'b')

        plt.savefig('images/puntopkaart.png', bbox_inches='tight', pad_inches=0)

    def print_connections(self):
        """Prints all connections between the stations"""
        for i in range(len(self.connections)):
            x_points = []
            y_points = []

            # Extracts the names for the first and second station which are connected
            station1, station2 = self.connections[i][0], self.connections[i][1]
            
            # Extract coordinates for the first station
            xpt1, ypt1 = self.correctcoords[station1][0], self.correctcoords[station1][1]
            x_points.append(xpt1)
            y_points.append(ypt1)

            # Extracts coordinates for the second station
            xpt2, ypt2 = self.correctcoords[station2][0], self.correctcoords[station2][1]
            x_points.append(xpt2)
            y_points.append(ypt2)

            self.m.plot(x_points, y_points, color = 'k', linewidth = 1)

        plt.savefig('images/lijnenopkaart.png', bbox_inches = 'tight', pad_inches = 0)

    def print_driven_routes(self, routes):
        """Takes the trainroutes and prints them on the map with colors for each different route"""
        colorcounter = 0
        trainroutes = routes

        # Loads in and loops over all trains with individual routes
        for trains in trainroutes:
            self.color_generator()
            
            tempstations = routes[trains]

            # Iterates over stations until the second to last station to plot the driven routes
            for i in range(1, len(tempstations) - 1, 1):
                x_coords = []
                y_coords = []

                # Sets the stations as source and destination
                source_station = tempstations[i]
                desintation_station = tempstations[i + 1]

                # Extracts coordinates for the first station
                xpt1, ypt1 = self.correctcoords[str(source_station)][0], self.correctcoords[str(source_station)][1]
                x_coords.append(xpt1)
                y_coords.append(ypt1)

                # Extracts coordinates for the second station
                xpt2, ypt2 = self.correctcoords[str(desintation_station)][0], self.correctcoords[str(desintation_station)][1]
                x_coords.append(xpt2)
                y_coords.append(ypt2)
                
                # Plots the connection between the stations on the map, using the generated colors for the particular route number
                self.m.plot(x_coords, y_coords, color = (self.colormap[colorcounter][0], self.colormap[colorcounter][1], self.colormap[colorcounter][2]), linewidth = 1)
            
            # Moves to the next point in the color library to avoid using the same colors
            colorcounter += 1

        plt.savefig('images/routesopkaart.png', bbox_inches = 'tight', pad_inches = 0)
        # Necessary to prevent map from being drawn into histogram
        plt.close()

    def statsplot_routes(self):
        """Plots most visited stations and most succesfull routes in the algorithms
           Aims to discover patterns in generated data"""
        pass

    def color_generator(self):
        """Generates random number combinations to get unique colors for trainroutes"""
        while True:
            
            colorlist = []
            for i in range(3):
                rand_col = 0
                while rand_col <= 0.1:
                    rand_col = random.random()
                rand_col = round(rand_col, 1)
                colorlist.append(rand_col) 

            if colorlist not in self.colormap:
                self.colormap.append(colorlist)
                return False
        
    def map_to_gif(self):
        """Takes all generated PNG's and creates an animated .gif for visualisation."""
        pass

class ResultStats():
    def __init__(self, experi_results):
        # Initialiseert de module met de uitkomsten van de experimenten
        self.results = experi_results

    def draw_hist(self):
        """Uses the provided soltuions and draws a histogram to plot the results"""
        
        self.results.hist(bins = 10, edgecolor = 'black')

mappings = Mapdrawer()
mappings.print_to_image()
mappings.print_connections()




# TODO: Visualisaties van meest bezochte stations in histogram etc