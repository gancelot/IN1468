"""

    02_as_dicts.py

"""
import linecache


class City:
    """ Encapsulates information about a city containing a population over 15,000"""
    def __init__(self, name, country='', population=0, elevation=-1):
        self.name = name
        self.country = country
        self.population = population
        self.elevation = elevation

    def __str__(self):
        return self.name


city_data = linecache.getline('../resources/cities15000.txt', 22237).strip().split('\t')
c = City(city_data[1], city_data[8], city_data[14], city_data[15])

print(c.__dict__['name'])
print(vars(c)['name'])
