import json
import os


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def to_json(self):
        return json.dumps(vars(self))


p = Person('Bob', 37)
p.address = '123 Main St.'
print(p._age)

