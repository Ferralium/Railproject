import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
from matplotlib import image

import matplotlib

# Rework data to useable format
# TODO: Has to come after calculating scale to get correct coordinates at once
correctcoords = []
with open("data/StationsHollandCoords.csv") as f:
    next(f)
    for line in f:
        tempcoords = []
        templine = line.strip().split(',')
        tempcoords.append(templine[1])
        tempcoords.append(templine[2])
        correctcoords.append(tempcoords)

class Mapdrawer():

    def __init__(self):
        # Example from (https://www.geeksforgeeks.org/python-save-list-to-csv/)
        np.savetxt('data/fixedcoords.csv', correctcoords, delimiter = ',', fmt ='% s')

        # Dimensions for the picture: Upper left: (53.491, 3.279) Lower right: (50.730, 7.295)
        data_path = 'data/fixedcoords.csv'
        data = pd.read_csv(data_path, names=['LATITUDE', 'LONGITUDE'], sep=',')

        self.gps_data = tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))


        self.pixelheight = 734
        self.pixelwidth = 819


    def scale_to_image(self):
        """Aims to rescale coordinates to pixel scale on the map .png"""
        self.coordlist = []
        for d in self.gps_data:
            templist = []
            x_pixel = (d[0] - 53.491) / (50.730 - 53.491) * self.pixelwidth
            y_pixel = (d[1] - 3.279) / ( 7.295 - 3.279) * self.pixelheight
            templist.append(x_pixel)
            templist.append(y_pixel)
            self.coordlist.append(templist)
            
    def print_to_image(self):
        """Prints the coordinates to the map image as dots"""
        data = image.imread('data/KaartScreenshot.png')

        for i in range(len(self.coordlist)):
            plt.plot(self.coordlist[i][0], self.coordlist[i][1], marker = '.')

        plt.imshow(data)
        plt.savefig('puntopkaart.png', bbox_inches='tight', pad_inches=0, transparent=True)
        

mappings = Mapdrawer()
mappings.scale_to_image()
mappings.print_to_image()

# TODO: Implementeer dit in de image functie, haal overige code weg
# Plotten op een afbeelding via matplotlib, werkt op de coordinaten