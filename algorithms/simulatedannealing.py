import random
# voor deze hillclimber er per stap
# - 2 keer een random start state worden gekozen


class SimulatedAnnealing:

    def __init__(self):
        """ Deze klas is de representatie van een hill climber algoritme om het Rail NL probleem op te lossen """
        pass


    def starting_station(self, station_dictionary, statnames):
        """"Picks a purely random starting station from the list of all possible stations"""
        current_station = random.choice(list(station_dictionary.values()))
        print(f'random starting station: {current_station}')
        return current_station

    def quality_calc(self, fraction: float, list_of_numbers) -> None:
        T: int = list_of_numbers[1]
        Min: int = list_of_numbers[0]
        self.K: float = fraction*10000 - (T*100 + Min)
        self.quality = f'Quality: {self.K} = {fraction}*1000 - ({T}*100 + {Min})'
        print(self.quality)

        return self.K


    def move(self, current_station, train_stations, stations_dictionary):
        time = 0

        # voeg de current station toe aan de lijst
        train_stations.append(current_station)
        print(train_stations)

        while True:

            # Moves to next random connection that has not been visited yet
            possible_next_station: str | Station = random.choice(list(current_station.connections))
            next_station: Station = stations_dictionary.get(possible_next_station)


            all_time: int = time + current_station.connections.get(str(next_station))

            # stops if time is more than 3 hours
            if all_time > 180:
                print(f'hi {all_time}')
                print(f'this will be returned {time}')
                return train_stations, time
            else:
                time = time + current_station.connections.get(str(next_station))

            print(f' Current Station: {current_station}')
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))
            current_station: Station = stations_dictionary.get(str(next_station))

            # voeg current_station toe aan de lijst
            train_stations.append(current_station)

            print(f' Next Station: {current_station}')
            print(time)
            print(" ")




    def make_or_break_change(self, quality: float, quality_2: float, train_dictionary, train_dictionary_2):
        """ Function that makes or breaks the mutation """

        delta = quality_2 - quality
        print(f'delta: {delta}')

        if delta > 1:

            # voer nieuwe state sowieso in
            train_dictionary = train_dictionary_2
            quality = quality_2

        else:

            chance = 2**delta


            if chance >= 1:

                # voer nieuwe state in
                train_dictionary = train_dictionary_2
                quality = quality_2

            if chance > 0 and chance < 1:

                # afhankelijk van de kans, voer hem in:
                guess = random.uniform(0, 1)

                print(f'guess: {guess}')

                if guess < chance:

                    train_dictionary = train_dictionary_2
                    quality = quality_2


        short_tuple = [train_dictionary, quality]
        return short_tuple

    # def mutation(self):
    #     """ Functie die een kleine mutatie maakt op de huidige state. """
    #     pass
    #     # make a mutation on this random algorithm
    #
    #     # hierin wordt eventueel het uiteinde van een random trein aangepast
    #     # kies eerst een random getal tussen de 1 en 20, en een getal tussen 1 of 2 (begin of eind van de trein)
    #     random_change = random.randint(0,19)
    #     front_or_back = random.randint(1,2)
