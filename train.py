class Train:
    def __init__(self, trainnum, first_stop):
        self.train_name = f'train{trainnum}'
        self.route = [first_stop]
        self.train_score = 0
        self.last_station = first_stop

    def add_stop(self, stop_name, stop_score):
        self.route.append(stop_name)
        self.train_score += stop_score
        self.last_station = self.route[len(self.route) - 1]


    