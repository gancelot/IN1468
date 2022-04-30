from typing import NamedTuple, List

City = NamedTuple('City', [('name', str), ('population', int),
                           ('elevation', int), ('country', str)])


class CitySearch:
    def __init__(self, filepath: str):
        """
            :param filepath (str): Absolute or relative path to the data file
        """
        self.cities = []
        self.filepath = filepath
        self._read_data()

    def _read_data(self):
        """
            Reads from the file.  Private method.
        """
        with open(self.filepath, encoding='utf-8') as f:
            for line in f:
                fields = line.strip().split('\t')
                name = fields[1]
                country = fields[8]
                population = int(fields[14])
                elevation = int(fields[16])
                city = City(name, population, elevation, country)
                self.cities.append(city)

    def largest(self) -> City:
        return max(self.cities, key=lambda city: city.population)

    def highest(self) -> City:
        return max(self.cities, key=lambda city: city.elevation)

    def search(self, name: str) -> List[City]:
        """
            Searches the protected self.cities names
            :param name: (str) search substring to find within city names
            :return: (list) List of City data classes
        """
        results = []
        for item in self.cities:
            if name.lower() in item.name.lower():
                results.append(item)
        return results


c = CitySearch('../resources/cities15000.txt')
print(c.search('los angeles'))
print(c.highest().name)

