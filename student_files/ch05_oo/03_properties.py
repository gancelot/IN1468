"""

    03_properties.py

"""


class City:
    def __init__(self, name, country='', population=0, elevation=-1):
        self.name = name
        self.country = country
        self.population = population
        self.elevation = elevation

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, pop):
        self._population = 0
        if pop > 0:
            self._population = pop

    @property
    def elevation(self):
        return self._elevation

    @elevation.setter
    def elevation(self, elev):
        self._elevation = 0
        if -400 < elev < 30000:
            self._elevation = elev

    def __str__(self):
        return f'{self.name} {self._population} {self._elevation}'


c = City('New York City', 'USA', 8175133)
c.elevation = 10
print(c.population)


c = City('Cloudland', 'New Zealand', -30, 35500)
print(c)
