class Logger(object):    
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name


    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        filename = open(self.file_name, "w")
        filename.write(f"Calculating Herd Immunity")
        filename.write(f"Population: {pop_size}\nVaccination Percentage: {vacc_percentage}\nVirus Name: {virus_name}\nMortality Rate: {mortality_rate}\nReproduction Rate: {basic_repro_num}\nNumber of those Initially infected: {initial_infected}\n")
        filename.close()

    def log_interactions(self, time_step_number, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        filename = open(self.file_name, "a")
        filename.write(f"Number of steps: {time_step_number}\nNumber of Interactions: {number_of_interactions}\nNumber of New Infections: {number_of_new_infections}\n")
        filename.close()

    def log_infection_survival(self, time_step_counter, population_count, number_of_new_fatalities):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        filename = open(self.file_name, "a")
        filename.write(f"Step number: {time_step_counter}\nPopulation count: {population_count}\nNew Fatalities: {number_of_new_fatalities}")
        filename.close()

    def log_time_step(self, time_step_counter, new_deaths, new_infections, total_of_deaths, is_vaccinated):
        filename = open(self.file_name, "a")
        filename.write(f"Step Number: {time_step_counter}\nNumber of Newly Infected: {new_infections}\nNumber of New Deaths: {new_deaths}\nTotal Number of Deaths: {total_of_deaths}\nNumber of Individuals Vaccinated: {is_vaccinated}\n")
        filename.close()

    def final_results(self, total_of_deaths, total_infected, is_vaccinated):
        filename = open(self.file_name, "a")
        filename.write(f"Infected: {total_infected}\nFatalities: {total_of_deaths}\nVaccinated Population: {is_vaccinated}")
        filename.close()