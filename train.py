class Train:
    """Creates a train object"""
    def __init__(self, trainnum: int, first_stop: str) -> None:
        """numbers the object,
        creates a list of the route of the train, 
        counts the score of the train"""
        self.train_name: str = f'train{trainnum}'
        self.route: list[str] = [first_stop]
        self.train_score: int = 0
        self.last_station = first_stop

    def add_stop(self, stop_name: str, stop_score: int) -> None:
        """adds a stop to the route of the train,
        and adds the score of the route to the total score"""
        self.route.append(stop_name)
        self.train_score += stop_score
        self.last_station = self.route[len(self.route) - 1]


    