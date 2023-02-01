import random
from station import Station

class SimulatedAnnealing:
    """ Algorithm for Rail NL that creates a simulated annealing algorithm to optimize the solution. """

    def __init__(self, start_heuristic, move_heuristic):
        self.start_heuristic = start_heuristic
        self.move_heuristic = move_heuristic


    def starting_station(self, station_dictionary, statnames):
        """"Picks a starting station according to the heuristic """
        return self.start_heuristic(station_dictionary)


    def fraction_calc(self, stations_library) -> float:
        """Function calculates percentage of used connections"""

        connected = 0
        total = 0

        for station_name in stations_library:

            temporary_station = stations_library[station_name]

            number_of_connections = len(temporary_station.connections)
            total += number_of_connections

            for connecties in temporary_station.connection_visited:

                if temporary_station.connection_visited[connecties] == True:
                    connected += 1

        fraction: float = round(connected / total, 2)
        return fraction


    def quality_calc(self, fraction: float, list_of_numbers) -> None:
        """Calculates the quality of the driven routes"""

        T: int = list_of_numbers[1]
        Min: int = list_of_numbers[0]
        self.K: float = fraction*10000 - (T*100 + Min)
        quality_written = f'Quality: {self.K} = {fraction}*10000 - ({T}*100 + {Min})'

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

        mutated: Bool = True

        # calculate the difference between qualities of mutated and unmutated solution
        delta = quality_2 - quality_old

        # if this is higher than or equal to 0, implement the mutation
        if delta >= 0:

            train_dictionary = train_dictionary_2
            quality_old = quality_2
            total_time_each_train[chosen_one[0]] += change_in_time

        # if not, calculate the chance to implement the mutation
        else:

            chance = 2**delta

            if chance <= 0 or chance >= 1:
                print("FOUT !!!")


            guess = random.uniform(0, 1)

            # if the guess is lower than the chance, implement the change
            if guess <= chance:

                train_dictionary = train_dictionary_2
                quality_old = quality_2
                total_time_each_train[chosen_one[0]] += change_in_time

            else:

                mutated = False

        # reset delta to zero and return the train dictionary
        delta = 0
        short_tuple = [train_dictionary, quality_old]
        return short_tuple, mutated


    def reset_visiting_status(self, switching_stations, stations_library):
        """ Function that resets the visited-status of connections, in case a mutation is not persued. """


        # create string objects of stations
        string_knooppunt = str(switching_stations[2])
        string_oud_end = str(switching_stations[0])
        strin_oud_middle = str(switching_stations[1])
        string_new_middle = str(switching_stations[3])

        switching_stations_0_str = str(switching_stations[0])
        switching_stations_1_str = str(switching_stations[1])
        switching_stations_2_str = str(switching_stations[2])
        switching_stations_3_str = str(switching_stations[3])
        switching_stations_4_str = str(switching_stations[4])

        # visit the old route
        switching_stations[0].stationvisit(str(switching_stations[1]))
        switching_stations[1].stationvisit(str(switching_stations[0]))
        switching_stations[1].stationvisit(str(switching_stations[2]))
        switching_stations[2].stationvisit(str(switching_stations[1]))

        # unvisit the new route (if there is only one visit)
        if switching_stations[3].check_number_visits(string_knooppunt) <= 1:
            switching_stations[2].station_unvisit(str(switching_stations[3]))
            switching_stations[3].station_unvisit(str(switching_stations[2]))

        else:
            switching_stations[2].one_less_visit(str(switching_stations[3]))
            switching_stations[3].one_less_visit(str(switching_stations[2]))


        if switching_stations[4].check_number_visits(string_new_middle) <= 1:
            switching_stations[3].station_unvisit(str(switching_stations[4]))
            switching_stations[4].station_unvisit(str(switching_stations[3]))

        else:
            switching_stations[4].one_less_visit(str(switching_stations[3]))
            switching_stations[3].one_less_visit(str(switching_stations[4]))



    def stations_to_be_switched(self, train_dictionary_2, stations_library, total_time_each_train):
        """ Function that randomly chooses a mutation """

        # choose a random train and back or end  (also random)
        pick_train = random.choice(list(train_dictionary_2.keys()))
        front_or_back = random.randint(1,2)

        chosen_one = [pick_train, front_or_back]

    	# zoek deze op in de train_dictionary
        if front_or_back == 1:

            list_of_stations_for_mutation = train_dictionary_2[pick_train]
            chosen_one.append(list_of_stations_for_mutation)

            station_for_mutation = list_of_stations_for_mutation[2]

            old_station_for_mutation_end = list_of_stations_for_mutation[0]

            old_station_for_mutation_middle = list_of_stations_for_mutation[1]


            connections_for_mutation = station_for_mutation.connections

        else:

            list_of_stations_for_mutation = train_dictionary_2[pick_train]
            chosen_one.append(list_of_stations_for_mutation)

            length_traject = len(list_of_stations_for_mutation)
            station_for_mutation = list_of_stations_for_mutation[length_traject - 3]

            old_station_for_mutation_end = list_of_stations_for_mutation[length_traject - 1]

            old_station_for_mutation_middle = list_of_stations_for_mutation[length_traject - 2]

            connections_for_mutation = station_for_mutation.connections


        new_station_for_mutation_middle: Station = random.choice(list(connections_for_mutation.keys()))
        new_station_for_mutation_middle = stations_library[new_station_for_mutation_middle]

        # search connections for the middle station
        connections_for_mutation_middle = new_station_for_mutation_middle.connections

        # pick a random end station
        new_station_for_mutation_end: Station = random.choice(list(connections_for_mutation_middle.keys()))
        new_station_for_mutation_end = stations_library[new_station_for_mutation_end]

        # make it into a string
        knooppunt = str(station_for_mutation)
        knooppunt_middle_new = str(new_station_for_mutation_middle)
        knooppunt_middle_old = str(old_station_for_mutation_middle)

        length_total_time_each_train = len(total_time_each_train)
        length_train_dictionary = len(train_dictionary_2)
        if length_train_dictionary != length_total_time_each_train:
            print("HELPHELPHELP ERROR!!")
            print(f'length train dictionary: {length_train_dictionary}')
            print(f'length total time of each train: {length_total_time_each_train}')

        total_time_train = total_time_each_train[pick_train]

        # check the time it takes to get there
        time_new_connection = new_station_for_mutation_middle.connections[knooppunt]
        time_new_connection += new_station_for_mutation_end.connections[knooppunt_middle_new]

        time_old_connection = old_station_for_mutation_middle.connections[knooppunt]
        time_old_connection += old_station_for_mutation_end.connections[knooppunt_middle_old]

        time_difference = time_new_connection - time_old_connection
        time_spare = 180 - total_time_train

        # while the new track does not fit in 180 minutes, pick another new end for this train
        while time_spare < time_difference:

            new_station_for_mutation_middle: Station = random.choice(list(connections_for_mutation.keys()))
            new_station_for_mutation_middle = stations_library[new_station_for_mutation_middle]

            connections_for_mutation_middle = new_station_for_mutation_middle.connections

            new_station_for_mutation_end: Station = random.choice(list(connections_for_mutation_middle.keys()))
            new_station_for_mutation_end = stations_library[new_station_for_mutation_end]

            # create strings
            knooppunt = str(station_for_mutation)
            knooppunt_middle_new = str(new_station_for_mutation_middle)
            knooppunt_middle_old = str(old_station_for_mutation_middle)


            total_time_train = total_time_each_train[pick_train]

            time_new_connection = new_station_for_mutation_middle.connections[knooppunt]
            time_new_connection += new_station_for_mutation_end.connections[knooppunt_middle_new]

            time_old_connection = old_station_for_mutation_middle.connections[knooppunt]
            time_old_connection += old_station_for_mutation_end.connections[knooppunt_middle_old]

            time_difference = time_new_connection - time_old_connection
            time_spare = 180 - total_time_train

        # create a list with all the stations to be changed for returning
        switching_stations = [old_station_for_mutation_end, old_station_for_mutation_middle, station_for_mutation, new_station_for_mutation_middle, new_station_for_mutation_end]

        # if the station picked itself for a connection, print that there is an error  !!!
        if switching_stations[2] == switching_stations[3]:
            print("ERROR: nieuw midden is gelijk aan knooppunt !!! ")

        return switching_stations, chosen_one


    def mutation_small(self, train_dictionary_2, train_dictionary, switching_stations, chosen_one, stations_library):
        """ Function that makes changes needed for mutation """

        # create string objects from stations
        switching_stations_0_str = str(switching_stations[0])
        switching_stations_1_str = str(switching_stations[1])
        switching_stations_2_str = str(switching_stations[2])
        switching_stations_3_str = str(switching_stations[3])
        switching_stations_4_str = str(switching_stations[4])


        # Set the new route to visited
        switching_stations[2].stationvisit(switching_stations_3_str)
        switching_stations[3].stationvisit(switching_stations_2_str)
        switching_stations[3].stationvisit(switching_stations_4_str)
        switching_stations[4].stationvisit(switching_stations_3_str)

        # make from objects from switching_stations station_obect (in case they were strings)
        for i in range(len(switching_stations)):
            if type(switching_stations[i]) is str:
                switching_stations[i] = stations_library[switching_stations[i]]

        # unvisit the old route
        if switching_stations[1].check_number_visits(switching_stations_2_str) <= 1:
            switching_stations[2].station_unvisit(switching_stations_1_str)
            switching_stations[1].station_unvisit(switching_stations_2_str)

        else:
            switching_stations[2].one_less_visit(switching_stations_1_str)
            switching_stations[1].one_less_visit(switching_stations_2_str)

        if switching_stations[0].check_number_visits(switching_stations_1_str) <= 1:
            switching_stations[0].station_unvisit(switching_stations_1_str)
            switching_stations[1].station_unvisit(switching_stations_0_str)

        else:
            switching_stations[0].one_less_visit(switching_stations_1_str)
            switching_stations[1].one_less_visit(switching_stations_0_str)

        # change the new route in train_dictionary_2
        if chosen_one[1] == 1:

            list_of_stations_for_mutation = train_dictionary_2[chosen_one[0]]
            list_of_stations_for_mutation[0] = switching_stations[4]
            list_of_stations_for_mutation[1] = switching_stations[3]

            train_dictionary_2[chosen_one[0]] = list_of_stations_for_mutation

        else:

            list_of_stations_for_mutation = train_dictionary_2[chosen_one[0]]
            length_traject = len(list_of_stations_for_mutation)

            list_of_stations_for_mutation[length_traject - 1] = switching_stations[4]
            list_of_stations_for_mutation[length_traject - 2] = switching_stations[3]

            train_dictionary_2[chosen_one[0]] = list_of_stations_for_mutation


        # change the total time used
        change_in_time: float = 0
        old_station_end = switching_stations[0]
        old_station_middle = switching_stations[1]

        new_station_end = switching_stations[4]
        new_station_middle = switching_stations[3]

        temporary_name = switching_stations[1].connections[str(old_station_end)]
        temporary_name_middle = switching_stations[2].connections[str(old_station_middle)]

        change_in_time -= temporary_name
        change_in_time -= temporary_name_middle
        temporary_name_2_end = switching_stations[3].connections[str(new_station_end)]
        temporary_name_2_middle = switching_stations[2].connections[str(new_station_middle)]

        change_in_time += temporary_name_2_end
        change_in_time += temporary_name_2_middle

        return change_in_time, train_dictionary_2
