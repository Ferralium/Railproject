from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Rework data to useable format

class Mapdrawer():
    def __init__(self):
        """Initializes the mapdrawer, loads in the correct coordinates from the csv"""
        # Extracts correct coordinates from the CSV. Maps these to the station name as key
        # TODO: Conversie hier van coordinaten en opslaan zodat niet hoeft te gebeuren bij individuele functies
        self.correctcoords = {}
        with open("data/StationsNationaal.csv") as f:
            next(f)
            for line in f:
                tempcoords = []
                templine = line.strip().split(',')
                tempcoords.append(templine[1])
                tempcoords.append(templine[2])
                self.correctcoords[templine[0]] = tempcoords
                
        # Extracts the connections from the CSV
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
        self.m = Basemap(projection = 'mill', llcrnrlat = 50.730, llcrnrlon = 3.279, urcrnrlat = 53.491, urcrnrlon = 7.295, resolution = 'h')
        self.m.drawcoastlines()
        self.m.drawcountries(linewidth=1)
        self.m.fillcontinents(color = 'coral', lake_color = 'aqua')

        # Drawing points on the map
        for station in self.correctcoords:
            xcord, ycord = float(self.correctcoords[station][0]), float(self.correctcoords[station][1])
            xpt, ypt = self.m(ycord, xcord)
            self.m.plot(xpt, ypt, '.', markersize = 10, color = 'b')

        plt.savefig('puntopkaart.png', bbox_inches='tight', pad_inches=0)

    def print_connections(self):
        """Prints all connections between the stations"""
        # Pakt lijst met connecties
        # Print tussen de stations de connecties
        for i in range(len(self.connections)):
            stat1 = []
            stat2 = []

            # Extracts the names for the first and second station which are connected
            station1, station2 = self.connections[i][0], self.connections[i][1]

            # Extracts the X and Y Geo-coordinates for the first station, converts these and saves them to the coordinate lists
            x_coords1, y_coords1 = float(self.correctcoords[station1][0]), float(self.correctcoords[station1][1])
            xpt1, ypt1 = self.m(y_coords1, x_coords1)
            stat1.append(xpt1)
            stat2.append(ypt1)

            # Extracts the X and Y Geo-coordinates for the second station, converts these and saves them to the coordinate list
            x_coords2, y_coords2 = float(self.correctcoords[station2][0]), float(self.correctcoords[station2][1])
            xpt2, ypt2 = self.m(y_coords2, x_coords2)
            stat1.append(xpt2)
            stat2.append(ypt2)

            # Plots a line between the coordinates of the stations
            self.m.plot(stat1, stat2, color='k', linewidth = 1)

        plt.savefig('lijnenopkaart.png', bbox_inches = 'tight', pad_inches = 0)

    def print_driven_routes(self, routes):
        """Takes the trainroutes and prints them on the map with colors for each different route"""
        # TODO: Map routes via dictionary met als values de coordinaten en lijnen tussen de punten, op kleur per route
        trainnames = routes.keys()
        for trains in trainnames:
            tempstations = routes[trains]

            # Iterates over stations until the second to last station to plot the driven routes
            for i in range(1, len(tempstations) - 1, 1):
                stat1 = []
                stat2 = []

                # Sets the stations as source and destination
                source_station = tempstations[i]
                desintation_station = tempstations[i + 1]

                x_coords1, y_coords1 = float(self.correctcoords[source_station][0]), float(self.correctcoords[source_station][1])
                xpt1, ypt1 = self.m(y_coords1, x_coords1)
                stat1.append(xpt1)
                stat2.append(ypt1)

                x_coords2, y_coords2 = float(self.correctcoords[desintation_station][0]), float(self.correctcoords[desintation_station][1])
                xpt2, ypt2 = self.m(y_coords2, x_coords2)
                stat1.append(xpt2)
                stat2.append(ypt2)
                
                # TODO: Implement color generation module to pick a random color, ensuring it is unique amongst its peers
                self.m.plot(stat1, stat2, color ='RANGENCOLOR', linewidth = 1)

        # Take train routes and load them into a list/dict
        # Generate random colors based on the amount of trains, make sure no repeat of colors
        # Extract station names per train
        # Draw driven connections between stations using unique colors for each route
        plt.savefig('routesopkaart.png', bbox_inces = 'tight', pad_inches = 0)

    def statsplot_routes(self):
        """Plots most visited stations and most succesfull routes in the algorithms
           Aims to discover patterns in generated data"""
        pass
        

mappings = Mapdrawer()
mappings.print_to_image()
mappings.print_connections()



# TODO: Visualisaties van meest bezochte stations in histogram etc