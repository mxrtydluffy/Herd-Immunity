import random
random.seed(42)
from virus import Virus


class Person(object):
    def __init__(self, _id, is_vaccinated, infection = None):

        """
        Person has an id which needs to be an int,
        is_vaccinated and possibly an infection
        self.is_alive and self.infected is a boolean
        """

        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True
        self.infected = False

    """
    Line #33 - Generates a random number.
    Random.random is used since it returns a random number and it's 
    generated to determine those who are sustainable of surviving.
    After Line #33 - If the number is less than the infection, the mortality rate 
    of the person's infection can happen 3 ways. (1) They are not vaccinated
    and they died, (2) they are vaccinated, (3) they weren't infected.
    """

    def did_survive_infection(self):
        if self.infection:
            random_soul = random.random()
            if random_soul < self.infection.mortality_rate:
                self.is_alive = False
                self.infection = None
                return False
            else:
                self.is_vaccinated = True
                self.infection = None
                return True
        else:
            return True
            

if __name__ == "__main__":

    """
    Defined vaccianted person and ther attributes begiining with Person(2, False)
    """

    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None


    unvaccinated_person = Person(2, False)
    
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None
    
    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)

    """
    Tested assert values of each attributes of the person
    """ 

    assert infected_person.id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert vaccinated_person.infection is virus


    """
    Created supply of 100 unvaccinated individuals
    """

    people = []
    for i in range(1, 101):
        # TODO Make a person with an infection
        # TODO Append the person to the people list
        person = Person (i, False, virus)
        people.append(person)

    did_survive = 0
    did_not_survive = 0

    """
    Initially needs to be 0 since we need to document. For each person that
    has survived, values are incremented by one. The same goes for those who
    didn't. Here we need to loop over all the people knowing who survived and
    who didn't
    """

    for person in people:
        has_survived = person.did_survive_infection() 
        if has_survived:
            did_survive += 1
        else:
            did_not_survive


    # Need to print to terminal
    print("_________________________________")
    print(f" Survived: {did_survive}")
    print(f" Deceased: {did_not_survive}")
    print("_________________________________")


    # ______________________________________________________

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 


    noninfected_people = []
    infected_people = []

    for i in range(1, 101):
        uninfected = Person(i, False)
        noninfected_people.append(person)

    for person in noninfected_people:
        random_num = random.random() 
        if random_num < virus.repro_rate:
            person.infection = virus
            infected_people.append(person)

    print(f"Reproductive Rate of an estimated amount of 100 people. {len(infected_people)} were the results.")
