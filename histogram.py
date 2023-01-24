import matplotlib.pyplot as plt

class StatsDrawer:
    def __init__(self):
        self.scorenumbers = []

        with open('results/score.txt') as f:
            for line in f:
                self.scorenumbers.append(float(line))

    def draw_hist(self):
        plt.hist(self.scorenumbers, bins = 20, edgecolor = 'black')
        plt.xlabel("Score", fontsize=13)
        plt.ylabel("Frequency", fontsize=13)
        plt.savefig('images/resultshistogram.png', dpi = 800)
        plt.close()

histoplot = StatsDrawer()
histoplot.draw_hist()
