import random
# random.seed(42)
from virus import Virus


class Person(object):
    def __init__(self, _id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = False
        self.is_alive = True

    """
    Line #26 - Only called if infection attribute is not None.
    Line #28 - Generates a random number between 0.0 - 1.0.
    Random.uniform is used since it returns a floating number
    between 0-1. This random number is generated to determine 
    those who are sustainable of surviving.
    Line #36 - If the number is less than the infection.mortality rate of 
    the person's infection it can happen 3 ways. (1) They are not vaccinated
    and they died, (2) they are vaccinated, (3) they weren't infected.
    """

    def did_survive_infection(self):
        if self.infection is not None:
            self.infection = True
            check_survival = random.uniform(0, 1)                              # check_survival = random.randint(0.0,1.0)
            if check_survival < self.infection.mortality_rate:
                self.is_vaccinated = False
                self.is_alive = False
                return self.is_alive
            else:
                self.is_vaccinated = True
                return self.is_alive
        else:
            self.is_infected = False
            return self.is_alive
            

if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    # TODO Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO Test unvaccinated_person's attributes here... | Remember to release in terminal
    print("_________________________________")
    print(unvaccinated_person._id)
    print(unvaccinated_person.is_vaccinated)
    print(unvaccinated_person.infection)
    print("_________________________________")

    
    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values of each attribute
    # assert ...

    """
    Tested values of each attributes of the person
    """ 

    assert infected_person.id == 3
    assert infected_person.is_alive is True or False
    assert infected_person.is_vaccinated is False
    assert vaccinated_person.infection is not None
    print('f Is alive: {infected_person.did_survive_infecton()}')


    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people

    """
    Created supply of 100 unvaccinated individuals
    """

    people = []
    for i in range(1, 100):
        # TODO Make a person with an infection
        # TODO Append the person to the people list
        infected = Person (i, False, virus)
        people.append(infected)

    # Now that you have a list of 100 people. Resolve whether the Person 
    # survives the infection or not by looping over the people list. 

    # for person in people:
    #     # For each person call that person's did_survive_infection method
    #     survived = person.did_survive_infection()

    # Count the people that survived and did not survive: 
   
    # did_survived = 0
    # did_not_survive = 0

    # TODO Loop over all of the people 
    # TODO If a person is_alive True add one to did_survive
    # TODO If a person is_alive False add one to did_not_survive


    """
    Initially needs to be 0 since we need to document. For each person that
    has survived, values are incremented by one. The same goes for those who
    didn't
    """

    survived = 0
    did_not_survive = 0
    for person in people:
        if person.did_survive_infection():
            survived += 1
        else:
            did_not_survive += 1

    print("_________________________________")
    print(f" Survived: {survived}")
    print(f" Decease: {did_not_survive}")

    
    # TODO When the loop is complete print your results.
    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people 
    # should succumb. 

    # ______________________________________________________

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 

    # _________________TEST #1_________________

    uninfected_people = []

    for i in range(1, 100):
        uninfected = Person(i, False)
        uninfected_people.append(uninfected)

    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected.

    got_infected = 0
    immune = 0

    # Assign the virus to that person's infection attribute. 

    for person in uninfected_people:
        immunity = random.uniform(0, 1)
        if immunity < virus.repro_rate:
            person.infection = virus
            got_infected += 1
        else:
            immune += 1
    
    print("_________________________________")
    print(f'Infected: {got_infected}')
    print(f'Immune: {immune}')
    print("_________________________________")


    # _________________TEST #2_________________

    """
    #178-179 is the virus info and information about
    the second person.
    #183-187 is determining the attributes of the person.
    """

    virus2 = Virus('Diphtheria', 0.65, 0.40)
    second_person = Person(1, False, virus2)

    assert second_person._id == 1
    assert second_person.is_vaccinated is False
    assert second_person.infection is not None
    assert second_person.did_survive_infection() is False
    assert second_person.is_infected is True


    # _________________TEST #3_________________

    """
    #196-199 is the reflecting those who were infected
    #202-208 shows who did survive the infection and those
    who didn't
    """

    diphtheria_people = []
    for i in range(1, 100):
        diphtheria_infected = Person(i, False, virus2)
        diphtheria_people.append(diphtheria_infected)

    survived_diphtheria = 0
    did_not_survive_diphtheria = 0
    for person in diphtheria_people:
        if person.did_survive_infection():
            survived_diphtheria += 1
        else:
            did_not_survive_diphtheria += 1

    assert survived_diphtheria == 0



    print(f'Survived COVID: {survived_diphtheria}')
    print(f'COVID Deaths: {did_not_survive_diphtheria}')
