from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Rework data to useable format

class Mapdrawer():
    def __init__(self):
        """Initializes the mapdrawer, loads in the correct coordinates from the csv"""
        self.correctcoords = []
        with open("data/StationsNationaal.csv") as f:
            next(f)
            for line in f:
                tempcoords = []
                templine = line.strip().split(',')
                tempcoords.append(templine[1])
                tempcoords.append(templine[2])
                self.correctcoords.append(tempcoords)
            
    def print_to_image(self):
        # Miller cylindrical projection
        m = Basemap(projection = 'mill', llcrnrlat = 50.730, llcrnrlon = 3.279, urcrnrlat = 53.491, urcrnrlon = 7.295, resolution = 'h')
        m.drawcoastlines()
        m.drawcountries(linewidth=1)
        m.fillcontinents(color = 'coral', lake_color = 'aqua')

        # Drawing points on the map
        for i in range(len(self.correctcoords)):
            xcord, ycord = float(self.correctcoords[i][0]), float(self.correctcoords[i][1])
            xpt, ypt = m(ycord, xcord)
            m.plot(xpt, ypt, '.', markersize = 10, color = 'b')

        plt.savefig('puntopkaart.png', bbox_inches='tight', pad_inches=0)
        

mappings = Mapdrawer()
mappings.print_to_image()

# TODO: Map routes via dictionary met als values de coordinaten en lijnen tussen de punten, op kleur per route
# TODO: Visualisaties van meest bezochte stations in histogram etc