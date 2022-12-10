import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger('simulation_test.txt') # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.newly_infected = []
        self.time_step_number = 0
        self.number_new_infections = 0
        self.total_vax = 0
        self.vax_saves = 0
        self.interactions = 0
        self.final_survivors = 0
        self.fatalities = 0
        self.final_infections = 0
        self.mankind = self._create_population(vacc_percentage, initial_infected)
        

        
        self.people = self._create_population()

        # TODO: Store the virus in an attribute
        # TODO: Store pop_size in an attribute
        # TODO: Store the vacc_percentage in a variable
        # TODO: Store initial_infected in a variable
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.
        pass

    def _create_population(self, vacc_percentage, inital_infected):
        # Vital to prioritize infected
        vaccinate_pop = int(round(self.pop_size * vacc_percentage))
        print(f'Current Vaccination Population: {vaccinate_pop}')
        total_population = []
        for i in range (self.pop_size):
            if self.initial_infected > 0:
                total_population.append(Person(i, False, self.virus))
                inital_infected -= 1
            elif self.vaccinate_pop > 0:
                total_population.append(Person(i, True))
                vaccinate_pop -= 1
            else:
                total_population.append(Person(i, False))
            
        return total_population
            
        # Next need to reset inorder to deal with uninfected
        # id = self.initial_infected + 1

        # # Uninfected population
        # for i in range (self.pop_size - self.initial_infected):
        #     uninfected_people = Person(id, False)
        #     people.append(uninfected_people)
        #     id += 1
        
        # return people


        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        # TODO: Return the list of people

    #_______________________Fix Bottom later___________________________

    def _simulation_should_continue(self):

        """
        Looping over all the list of people in the population doumenting
        those who are dead and adding thme to dead count and comparing to
        the population as a whole.
        """

        vax_counter = 0
        dead_counter = 0
        document_counter = 0

        for person in self.mankind:
            if person.is_alive and not person.is_vaccinated:
                counter += 1
            elif person.is_alive and person.is_vaccinated:
                vax_counter += 1
            elif not person.is_alive:
                dead_counter += 1

        print(f'Current Vax: {vax_counter}\Current Deaths: {dead_counter}\nAlive & unvax: {document_counter}')


        # Simulation will 
        if counter > 0:
            return True
        else:
            return False


        # survivors = len(self.people)
        # vaccinated = 0
        # while survivors > 0 or vaccinated < len(self.people):
        #     for person in self.people:
        #         if person.survived != True:
        #             survivors -= 1
        #         if person.is_vaccinated != False:
        #             vaccinated += 1
        #     return True
        # return False

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        should_continue = True
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while should_continue:
            # TODO: Increment the time_step_counter
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue

            """
            #136-140 Increments the time step counter
            #143-145 Determines final results
            """

            self.time_step_number += 1
            print(f'Current Time Step: {self.time_step_number}')
            self.time_step()
            self.logger.log_interactions(self.time_step_number, self.interactions, self.number_new_infections)
            should_continue = self._simulation_should_continue()

        for person in self.mankind:
            if person.infection is not None:
                self.final_infections += 1

        for person in self.society:
            if person.is_vaccinated:
                self.total_vax += 1
                self.final_survivors += 1
            elif not person.is_alive:
                self.fatalities +=1


        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 

        self.logger.final_data(self.final_survivors, self.fatalities, self.final_infections, self.total_vax, self.interactions, self.number_new_infections, self.vax_saves)
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        

        people_alive = [person for person in self.society if person.is_alive]

        if len(self.society) > 100:
            random_group = random.sample(people_alive, k=100)
        else:
            random_group = people_alive

        sick_people = [person for person in self.society if person.infection is not None]

        for sick_person in sick_people:
            for random_person in random_group:
                self.interaction(sick_person, random_person)
                self.interactions += 1

        self._infect_newly_infected()

        for person in self.society:
            if person.did_survive_infection():
                self.vax_saves += 1


    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        
        if random_person.infection is None and not random_person.is_vaccinated:
            chance = random.random()

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            person.infection = self.virus
            self.number_new_infections += 1
        
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()
