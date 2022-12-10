# Properties and attributes of the virus used in Simulation.

class Virus(object):
    def __init__(self, name, repro_num, mortality_rate):
        self.name = name
        self.repro_num = repro_num
        self.mortality_rate = mortality_rate


"""
Testing this virus class by making an instance and confirming 
it has the attributes that is defined.
"""

if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_num == 0.8
    assert virus.mortality_rate == 0.3

"""
Additional Virus tests
"""

virus2 = Virus("Diphtheria", 6.5, 0.40)
assert virus2.name == "Diphtheria"
assert virus2.repro_num == 6.5
assert virus2.mortality_rate == 0.40

virus3 = Virus("Polio", 0.70, 0.48)
assert virus3.name == "Polio"
assert virus3.repro_num == 0.70
assert virus3.mortality_rate == 0.48