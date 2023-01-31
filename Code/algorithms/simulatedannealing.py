## algoritme met grote mutaties

import random
from station import Station
# voor deze hillclimber wordt er een greedy algoritme gebruikt, dus dat is
# een slim start station en slimme moves!


class SimulatedAnnealing:
    """ Class that creates a simulated annealing algorithm to solve the case. """

    def __init__(self, start_heuristic, move_heuristic):
        """ Deze klas is de representatie van een hill climber algoritme om het Rail NL probleem op te lossen """
        self.start_heuristic = start_heuristic
        self.move_heuristic = move_heuristic


    def starting_station(self, station_dictionary, statnames):
        """"Picks a starting station with the least connections """
        return self.start_heuristic(station_dictionary)


    def fraction_calc(self, stations_library) -> float:
        """Function calculates percentage of used connections"""

        print("Calculate franction of used connections")
        print()
        connected = 0
        total = 0

        for station_name in stations_library:

            temporary_station = stations_library[station_name]

            # print(station_name, temporary_station.connection_visited)
            # number_of_connections = len(temporary_station.connection_visited)
            number_of_connections = len(temporary_station.connections)
            # print(f'aantal connecties: {number_of_connections}')
            total += number_of_connections

            for connecties in temporary_station.connection_visited:

                # print(temporary_station, connecties, temporary_station.connection_visited[connecties])

                if temporary_station.connection_visited[connecties] == True:
                    connected += 1

        # print(f' Connected: {connected}, Total: {total}') UITGEZET
        fraction: float = round(connected / total, 2)

        return fraction


    def quality_calc(self, fraction: float, list_of_numbers) -> None:

        # als de trein langer rijdt dan 180 minuten, mag het niet worden ingevoerd want de oplossing is ongeldig
        # zet dan de K op 0, dan is de kans op invoering extreem klein
        # if list_of_numbers[0] > 180:
        #     self.K = 0
        #     return self.K

        T: int = list_of_numbers[1]
        Min: int = list_of_numbers[0]
        self.K: float = fraction*10000 - (T*100 + Min)
        quality_written = f'Quality: {self.K} = {fraction}*10000 - ({T}*100 + {Min})'
        print("in quality calc")
        print(quality_written)


        return self.K, quality_written


    def move(self, current_station, train_stations, stations_dictionary):
        """ Moves to a smart next station """
        time: float = 0
        train_stations.append(current_station)

        if current_station == None:
            return train_stations, time

        # one loop is a move from station A to station B
        while True:
            next_station: Station = self.move_heuristic(current_station, train_stations, stations_dictionary)
            if next_station is None:
                return train_stations, time

            # keeps track of the time the trajectory takes
            all_time: float = time + current_station.connections.get(str(next_station))

            # stops if time is more than 3 hours
            if all_time > 180:
                return train_stations, time
            else:
                time = all_time

            # sets connections to and from to visited
            current_station.stationvisit(str(next_station))
            next_station.stationvisit(str(current_station))

            current_station = next_station
            train_stations.append(current_station)


    def make_or_break_change(self, quality_old: float, quality_2: float, train_dictionary, train_dictionary_2, change_in_time, total_time_each_train, chosen_one):
        """ Function that makes or breaks the mutation """

        # Quality old was de kwaliteit van de vorige loop. Als Quality_2 beter is of de kans het zegt,
        # veranderen we Quality_old in Quality_2. Anders blijft het hetzelfde
        # Quality_old returnen we vervolgens.

        mutated: Bool = True
        delta = quality_2 - quality_old
        # print(f'delta: {delta}') UITGEZET

        if delta >= 0:

            # voer nieuwe state sowieso in
            train_dictionary = train_dictionary_2
            quality_old = quality_2
            # voer de change in time ook in in de dictionary v
            total_time_each_train[chosen_one[0]] += change_in_time
            # print("mutation accepted, verbetering of gelijk") UITGEZET
            # print(f'the train has now ridden {total_time_each_train[chosen_one[0]]} min') UITGEZET


        else:

            chance = 2**delta

            if chance <= 0 or chance >= 1:
                print("FOUT !!!")


                # afhankelijk van de kans, voer hem in:
            guess = random.uniform(0, 1)

            # print(f'guess: {guess}') UITGEZET

            if guess <= chance:

                train_dictionary = train_dictionary_2
                quality_old = quality_2
                total_time_each_train[chosen_one[0]] += change_in_time
                # print(f'the train has now ridden {total_time_each_train[chosen_one[0]]} min')UITGEZET
                # print("mutation accepted, chance says so")UITGEZET

            else:
                # print("mutation not accepted, chance too low")UITGEZET
                # voer de change in time terug
                ## BUG Fixen!!!
                print("?? chance tussen 0 en 1 ")

                # zet changed op False
                mutated = False


        delta = 0
        short_tuple = [train_dictionary, quality_old]
        return short_tuple, mutated


    def reset_visiting_status(self, switching_stations, stations_library):
        """ Function that resets the visited-status of connections, in case a mutation is not persued after all. """

        # zet de nieuwe route die niet doorgaat op unvisited, maar alleen als er maar 1 visit is
        # print("     reset visiting status")UITGEZET
        # print()UITGEZET

        # maak eerst even string objecten van
        string_knooppunt = str(switching_stations[2])
        string_oud_end = str(switching_stations[0])
        strin_oud_middle = str(switching_stations[1])
        string_new_middle = str(switching_stations[3])

        # zet oude route op visited
        switching_stations[0].stationvisit(str(switching_stations[1]))
        switching_stations[1].stationvisit(str(switching_stations[0]))
        switching_stations[1].stationvisit(str(switching_stations[2]))
        switching_stations[2].stationvisit(str(switching_stations[1]))

        # zet de nieuwe route op unvisited (alleen als daar geen andere treinen meer rijden)
        # eerst van knooppunt naar middle
        if switching_stations[3].check_number_visits(string_knooppunt) <= 1:
            switching_stations[2].station_unvisit(str(switching_stations[3]))
            switching_stations[3].station_unvisit(str(switching_stations[2]))

        else:
            switching_stations[2].one_less_visit(str(switching_stations[3]))
            switching_stations[3].one_less_visit(str(switching_stations[2]))

        # nu van new_middle naar new_end
        if switching_stations[4].check_number_visits(string_new_middle) <= 1:
            switching_stations[3].station_unvisit(str(switching_stations[4]))
            switching_stations[4].station_unvisit(str(switching_stations[3]))

        else:
            switching_stations[4].one_less_visit(str(switching_stations[3]))
            switching_stations[3].one_less_visit(str(switching_stations[4]))


    def stations_to_be_switched(self, train_dictionary_2, stations_library, total_time_each_train):
        """ Functie die willekeurig uitkiest welke connecties worden gemuteerd. """

        # kies eerst willekeurig welke trein en welk uiteinde wordt verlegt.
        pick_train = random.choice(list(train_dictionary_2.keys()))
        # print(f'trein die gemuteerd word: {pick_train}')UITGEZET
        front_or_back = random.randint(1,2)

        chosen_one = [pick_train, front_or_back]

    	# zoek deze op in de train_dictionary
        if front_or_back == 1:
            # print("change front of train")UITGEZET

            # pak de lijst van de stations
            list_of_stations_for_mutation = train_dictionary_2[pick_train]
            # print(f' route van gekozen trein: {list_of_stations_for_mutation}')UITGEZET
            chosen_one.append(list_of_stations_for_mutation)

            # ga naar het 3e station in de lijst
            station_for_mutation = list_of_stations_for_mutation[2]

            # print(f'dit is het knooppuntstation: {station_for_mutation}')UITGEZET
        	# print(type(station_for_mutation))
            old_station_for_mutation_end = list_of_stations_for_mutation[0]
            # print(f'oude station uiteinde: {old_station_for_mutation_end}')UITGEZET

            old_station_for_mutation_middle = list_of_stations_for_mutation[1]
            # print(f'oude station midden: {old_station_for_mutation_middle}')UITGEZET


            connections_for_mutation = station_for_mutation.connections
            # print(f'dit zijn de connecties: {connections_for_mutation}')UITGEZET

        else:
            # print("change back of train")UITGEZET

            # list_of_stations_for_mutation = train_dictionary_2[pick_train]
            # chosen_one.append(list_of_stations_for_mutation)
            # length_traject = len(list_of_stations_for_mutation)
            #
        	# # ga naar het 2e station in de lijst
            # station_for_mutation = list_of_stations_for_mutation[length_traject - 2]
            #
            # print(f'dit is het knooppuntstation: {station_for_mutation}')
            #
            # old_station_for_mutation = list_of_stations_for_mutation[length_traject - 1]
            # print(f' route van trein: {list_of_stations_for_mutation}')
            #
            # print(f'oud station: {old_station_for_mutation}')
            #
            # connections_for_mutation = station_for_mutation.connections
            # print(f'dit zijn de connecties: {connections_for_mutation}')

            ## MET 2 STATIONS!!!
            list_of_stations_for_mutation = train_dictionary_2[pick_train]
            # print(f'wat gaat er mis met het oude station? {list_of_stations_for_mutation}')UITGEZET
            chosen_one.append(list_of_stations_for_mutation)

            # ga naar het 3e station in de lijst
            length_traject = len(list_of_stations_for_mutation)
            station_for_mutation = list_of_stations_for_mutation[length_traject - 3]

            # print(f'dit is het knooppuntstation: {station_for_mutation}')UITGEZET
        	# print(type(station_for_mutation))
            old_station_for_mutation_end = list_of_stations_for_mutation[length_traject - 1]
            # print(f'oude station uiteinde: {old_station_for_mutation_end}')UITGEZET

            old_station_for_mutation_middle = list_of_stations_for_mutation[length_traject - 2]
            # print(f'oude station midden: {old_station_for_mutation_middle}')UITGEZET


            connections_for_mutation = station_for_mutation.connections
            # print(f'dit zijn de connecties van het knooppunt: {connections_for_mutation}')UITGEZET


        ## kies een nieuwe route uit:

        # eerst voor het 'midden' station
        new_station_for_mutation_middle: Station = random.choice(list(connections_for_mutation.keys()))
        new_station_for_mutation_middle = stations_library[new_station_for_mutation_middle]

        # zoek daarvan de connecties op:
        connections_for_mutation_middle = new_station_for_mutation_middle.connections

        # en kies daar weer een random station voor:
        new_station_for_mutation_end: Station = random.choice(list(connections_for_mutation_middle.keys()))
        new_station_for_mutation_end = stations_library[new_station_for_mutation_end]

        # maak even een string van het knooppunt station
        knooppunt = str(station_for_mutation)
        knooppunt_middle_new = str(new_station_for_mutation_middle)
        knooppunt_middle_old = str(old_station_for_mutation_middle)

        # print(f'total time each train: {total_time_each_train}')UITGEZET
        # print(f'train dictionary: {train_dictionary_2}')UITGEZET
        length_total_time_each_train = len(total_time_each_train)
        length_train_dictionary = len(train_dictionary_2)
        if length_train_dictionary != length_total_time_each_train:
            print("HELPHELPHELP ERROR!!")
            print(f'length train dictionary: {length_train_dictionary}')
            print(f'length total time of each train: {length_total_time_each_train}')

        # print("train dictionary and total time each train should have the same number of trains..")UITGEZET
        total_time_train = total_time_each_train[pick_train]

        # nu kijken wat de tijd is om daar te komen:
        time_new_connection = new_station_for_mutation_middle.connections[knooppunt]
        time_new_connection += new_station_for_mutation_end.connections[knooppunt_middle_new]

        time_old_connection = old_station_for_mutation_middle.connections[knooppunt]
        time_old_connection += old_station_for_mutation_end.connections[knooppunt_middle_old]

        time_difference = time_new_connection - time_old_connection
        time_spare = 180 - total_time_train

        while time_spare < time_difference:


            ## kies een nieuwe route uit:
            # eerst voor het 'midden' station
            new_station_for_mutation_middle: Station = random.choice(list(connections_for_mutation.keys()))
            new_station_for_mutation_middle = stations_library[new_station_for_mutation_middle]

            # zoek daarvan de connecties op:
            connections_for_mutation_middle = new_station_for_mutation_middle.connections

            # en kies daar weer een random station voor:
            new_station_for_mutation_end: Station = random.choice(list(connections_for_mutation_middle.keys()))
            new_station_for_mutation_end = stations_library[new_station_for_mutation_end]

            # maak even een string van het knooppunt station
            knooppunt = str(station_for_mutation)
            knooppunt_middle_new = str(new_station_for_mutation_middle)
            knooppunt_middle_old = str(old_station_for_mutation_middle)


            total_time_train = total_time_each_train[pick_train]

            # nu kijken wat de tijd is om daar te komen:
            time_new_connection = new_station_for_mutation_middle.connections[knooppunt]
            time_new_connection += new_station_for_mutation_end.connections[knooppunt_middle_new]

            time_old_connection = old_station_for_mutation_middle.connections[knooppunt]
            time_old_connection += old_station_for_mutation_end.connections[knooppunt_middle_old]

            time_difference = time_new_connection - time_old_connection
            time_spare = 180 - total_time_train

        # return uiteindelijk de stations
        switching_stations = [old_station_for_mutation_end, old_station_for_mutation_middle, station_for_mutation, new_station_for_mutation_middle, new_station_for_mutation_end]
        return switching_stations, chosen_one


    def mutation_small(self, train_dictionary_2, train_dictionary, switching_stations, chosen_one, stations_library):
        """ Functie die gekregen stations omwisselt, en daarbij de tijd veranderd, en de visited routes veranderd. """

        switching_stations_0_str = str(switching_stations[0])
        switching_stations_1_str = str(switching_stations[1])
        switching_stations_2_str = str(switching_stations[2])
        switching_stations_3_str = str(switching_stations[3])
        switching_stations_4_str = str(switching_stations[4])

        # Zet de nieuwe route op visited
        switching_stations[2].stationvisit(switching_stations_3_str)
        switching_stations[3].stationvisit(switching_stations_2_str)
        switching_stations[3].stationvisit(switching_stations_4_str)
        switching_stations[4].stationvisit(switching_stations_3_str)



        # unvisit de oude route (als daar maar 1 visit staat)
        # string_knooppunt = str(switching_stations[2])
        # string_oud_end = str(switching_stations[0])
        # strin_oud_middle = str(switching_stations[1])

        # maak van alles in switching_stations station objecten
        for i in range(len(switching_stations)):
            if type(switching_stations[i]) is str:
                print("station object was een string. ")
                switching_stations[i] = stations_library[switching_stations[i]]

        # print(string_knooppunt, type(string_knooppunt))
        # print(switching_stations[1], type(switching_stations[1]))

        # eerst voor old_middle naar knooppunt
        if switching_stations[1].check_number_visits(switching_stations_2_str) <= 1:
            switching_stations[2].station_unvisit(switching_stations_1_str)
            switching_stations[1].station_unvisit(switching_stations_2_str)

        else:
            switching_stations[2].one_less_visit(switching_stations_1_str)
            switching_stations[1].one_less_visit(switching_stations_2_str)

        # nu van old_middle naar old_end
        if switching_stations[0].check_number_visits(switching_stations_1_str) <= 1:
            switching_stations[0].station_unvisit(switching_stations_1_str)
            switching_stations[1].station_unvisit(switching_stations_0_str)

        else:
            switching_stations[0].one_less_visit(switching_stations_1_str)
            switching_stations[1].one_less_visit(switching_stations_0_str)


        # verander het in de train_dictionary
        if chosen_one[1] == 1:

            list_of_stations_for_mutation = train_dictionary_2[chosen_one[0]]
            # list_of_stations_for_mutation[0] = switching_stations[2]
            list_of_stations_for_mutation[0] = switching_stations[4]
            list_of_stations_for_mutation[1] = switching_stations[3]

            train_dictionary[chosen_one[0]] = list_of_stations_for_mutation

        else:

            list_of_stations_for_mutation = train_dictionary_2[chosen_one[0]]
            length_traject = len(list_of_stations_for_mutation)

            # list_of_stations_for_mutation[0] = switching_stations[2]
            list_of_stations_for_mutation[length_traject - 1] = switching_stations[4]
            list_of_stations_for_mutation[length_traject - 2] = switching_stations[3]

            train_dictionary[chosen_one[0]] = list_of_stations_for_mutation


        # # verander ook de tijd:
        change_in_time: float = 0
        old_station_end = switching_stations[0]
        old_station_middle = switching_stations[1]

        new_station_end = switching_stations[4]
        new_station_middle = switching_stations[3]

        temporary_name = switching_stations[1].connections[str(old_station_end)]
        # print(f'min oude route einde {temporary_name}')UITGEZET
        temporary_name_middle = switching_stations[2].connections[str(old_station_middle)]
        # print(f'min oude route einde midden {temporary_name_middle}')UITGEZET

        change_in_time -= temporary_name
        change_in_time -= temporary_name_middle
        # change_in_time -= station_for_mutation.connections[old_station]
        temporary_name_2_end = switching_stations[3].connections[str(new_station_end)]
        # print(f'min nieuwe route einde {temporary_name_2_end}')UITGEZET
        temporary_name_2_middle = switching_stations[2].connections[str(new_station_middle)]
        # print(f'min nieuwe route einde {temporary_name_2_middle}')UITGEZET


        change_in_time += temporary_name_2_end
        change_in_time += temporary_name_2_middle

        # print(f'change in time: {change_in_time}')UITGEZET


        return change_in_time
