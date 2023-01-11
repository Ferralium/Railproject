import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw

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

# Example from (https://www.geeksforgeeks.org/python-save-list-to-csv/)
np.savetxt('data/fixedcoords.csv', correctcoords, delimiter = ',', fmt ='% s')

# Dimensions for the picture: Upper left: (53.491, 3.279) Lower right: (50.730, 7.295)
data_path = 'data/fixedcoords.csv'
data = pd.read_csv(data_path, names=['LATITUDE', 'LONGITUDE'], sep=',')

gps_data = tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))

image = Image.open('data/KaartScreenshot.png', 'r') # Load map image.
img_points = []

# for d in gps_data:
#     x1, y1 = plt.scale_to_img(d, (image.size[0], image.size[1]))
#     img_points.append((x1, y1))

heightscale = 53.491 - 50.730
widthscale = 3.279 - 7.295

print(heightscale)
print(widthscale)
