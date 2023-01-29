import matplotlib.pyplot as plt
import numpy as np

class StatsDrawer:
    def __init__(self):
        self.scorenumbers = []

        with open('results/score.txt') as f:
            for line in f:
                self.scorenumbers.append(float(line))

    def draw_hist(self):
        plt.hist(self.scorenumbers, bins = 20, edgecolor = 'black')
        plt.xlabel("Score", fontsize=13)
        plt.xticks(np.arange(5300, 6000, step=100))
        plt.ylabel("Frequency", fontsize=13)
        plt.yticks(np.arange(0, 3, step=1))
        plt.grid(True, linewidth=0.5, color='#757b82', linestyle='-')
        plt.savefig('images/resultshistogram.png', dpi = 800)
        plt.close()

histoplot = StatsDrawer()
histoplot.draw_hist()
