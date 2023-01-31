import matplotlib.pyplot as plt
import numpy as np

class StatsDrawer:
    def __init__(self, x):
        self.scorenumbers = []

        with open(f'../results/score{x}.txt') as f:
            for line in f:
                self.scorenumbers.append(float(line))

    def draw_hist(self, x):
        plt.hist(self.scorenumbers, bins = 20, edgecolor = 'black')
        plt.xlabel("Score", fontsize=13)
        plt.ylabel("Frequency", fontsize=13)
        plt.grid(True, linewidth=0.5, color='#757b82', linestyle='-')
        plt.savefig(f'../results/resultshistogram{x}.png', dpi = 800)
        plt.close()

while True:
    x = input('Which score? ')
    if x == 'stop':
        break
    histo = StatsDrawer(x)
    histo.draw_hist(x)
    