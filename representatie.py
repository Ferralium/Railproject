import numpy as np

# Rework data to useable format
correctcoords = []
with open("data/StationsHollandCoords.csv") as f:
    next(f)
    for line in f:
        tempcoords = []
        templine = line.strip().split(',')
        tempcoords.append(templine[1])
        tempcoords.append(templine[2])
        correctcoords.append(tempcoords)

np.savetxt('data/fixedcoords.csv', correctcoords, delimiter = ',', fmt ='% s')
# Dimensions for the picture: Upper left: (53.491, 3.279) Lower right: (50.730, 7.295)