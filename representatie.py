from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Rework data to useable format

class Mapdrawer():
    def __init__(self):
        """Initializes the mapdrawer, loads in the correct coordinates from the csv"""
        
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

        plt.savefig('puntopkaart.png', bbox_inches='tight', pad_inches=0)

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