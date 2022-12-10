import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):

        """
        Created Logger object and bind it to self.logger.
        Make sure to call the appropriate logger method 
        in all the nessesary parts of the simulation.
        """

        logger = Logger("logger.txt")
        self.logger = logger
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.total_infected = 0
        self.newly_infected = []
        self.infected_number = 0 
        self.is_vaccinated = 0
        self.new_deaths = 0 
        self.total_of_deaths = 0
        self.people = self._create_population()


    def _create_population(self):
        
        """
        In the population we need to know all the details of the people.
        Knowing this it's vital to prioritize the infected
        #42 is the list of people
        #46 represents the vaccinated group
        #51 stands for infected group
        #58 calculates the pop sice with infected and vaccinated people
        """

        people = []
        total_vaccinated = int(self.vacc_percentage * self.pop_size) 
        id = 0 
        
        for i in range(total_vaccinated):
            person = Person(id, True)
            people.append(person)
            id += 1

        for i in range(initial_infected):
            person = Person(id, False, self.virus)
            person.infected = True
            self.total_infected += 1
            people.append(person)
            id += 1

        for i in range(self.pop_size - self.initial_infected - total_vaccinated):
            person = Person(id, False)
            people.append(person)
            id += 1

        return people


    def _simulation_should_continue(self):

        """
        Looping over all the list of people in the population doumenting
        those who are dead and adding thme to dead count and comparing to
        the population as a whole.
        """

        print("Calculating Herd Immunity")
        print("_______Results may take a moment_______")

        pop = self.is_vaccinated + self.total_of_deaths
        if pop == self.pop_size: 
            self.logger.final_results(self.total_of_deaths, self.is_vaccinated)
            return False
        elif len(self.newly_infected) == 0:
            self.logger.final_results(self.total_of_deaths, self.total_infected, self.is_vaccinated)
            return False
        else:
            return True


    def run(self):

        """
        This method starts the simulation. It will track the number of 
        steps the simulation has run and check if the simulation should 
        continue at the end of each step.
        #104 should_continue increments time_step_counter by 1
        """

        time_step_counter = 0
        should_continue = True
        self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_num, self.initial_infected)
         

        while should_continue:

            time_step_counter += 1
            self.infected_number = 0
            self.new_deaths = 0
            self.interactions = 0
            self.time_step()
        
            self._if_survived()
            self.total_of_deaths += self.new_deaths
            should_continue = self._simulation_should_continue()

            if not should_continue:
                break

            self._infect_newly_infected()
            self.total_infected += self.infected_number

            self.logger.log_time_step(time_step_counter, self.new_deaths, self.infected_number, self.total_of_deaths, self.is_vaccinated)

    def time_step(self):

        """
        Oversees if random person is alive in population.
        """

        for person in self.people:
            if person.infection and person.is_alive:
                for i in range(101):
                    random_person = random.choice(self.people)
                    while not random_person.is_alive:
                        random_person = random.choice(self.people)
                    self.interaction(random_person)
        


    def interaction(self, random_person):

        """
        Evaluates if random person is alive who is vaccinated and no infection was present.
        """

        random_i = random.random() 

        if not random_person.is_vaccinated and not random_person.infection and random_person.is_alive:
            if random_i < self.virus.repro_num:
                self.newly_infected.append(random_person)


    def _infect_newly_infected(self):

        """
        If person infects people in the population
        """

        for person in self.newly_infected:
            if not person.infected:
                person.infection = self.virus
                person.infected = True
                self.infected_number += 1

        self.newly_infected = []


    def _if_survived(self):
        for person in self.people:
            if person.infection:
                did_survive = person.did_survive_infection()
                if not did_survive:
                    self.new_deaths += 1
                else:
                    self.is_vaccinated += 1


if __name__ == "__main__":

    virus_name = "Polio"
    repro_num = 0.4
    mortality_rate = 0.7
    virus = Virus(virus_name, repro_num, mortality_rate)

    pop_size = 575000
    vacc_percentage = 0.42
    initial_infected = 85

    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()