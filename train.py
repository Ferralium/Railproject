class Train:
    def __init__(self, trainnum, firststop):
        self.trainname = f'train{trainnum}'
        self.route = [firststop]
        self.trainscore = 0

    def add_stop(self, stopname, stopscore):
        self.route.append(stopname)
        self.trainscore += stopscore

    