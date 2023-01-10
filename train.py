class Train:
    def __init__(self, trainnum, firststop):
        self.trainname = f'train{trainnum}'
        self.route = [firststop]
        self.trainscore = 0
        self.laststation = firststop

    def add_stop(self, stopname, stopscore):
        self.route.append(stopname)
        self.trainscore += stopscore
        self.laststation = self.route[len(self.route) - 1]


    