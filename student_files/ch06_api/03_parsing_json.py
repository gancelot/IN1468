import dataclasses
import datetime
import json
import sys


data = r'''{"name":"Burns","results":[{"actor":"Christopher Collins (early season 1), Harry Shearer","episode_debut":"\"Simpsons Roasting on an Open Fire\"","name":"Charles Montgomery Burns","original_air_date":"1989-","role":"Owner of the Springfield Nuclear Power Plant."}]}'''

result = json.loads(data)
print(result.get('results')[0].get('name'))


with open('json_file_save.json', 'wt') as f:
    json.dump(result, f)


# -------------------------------------------------------------------------------
# The following shows how to handle a field that can't be serialized automatically

@dataclasses.dataclass
class Employee:
    first: str
    last: str
    salary: float
    hiredate: datetime.date


hired = datetime.date(1997, 10, 20)
empl = Employee('Thomas', 'Hanks', 22_000_000, hired)
try:
    json_str = json.dumps(vars(empl))
except TypeError as err:
    print(f'Error: {err}', file=sys.stderr)


# an easy fix for the error above...
json_str = json.dumps(vars(empl), default=str)
print(json_str)


class EmployeeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            result = vars(obj)
        except (AttributeError, TypeError):
            if isinstance(obj, datetime.date):
                result = obj.strftime('%Y-%b-%d')
            else:
                result = '(unknown type)'
        return result


print(json.dumps(vars(empl), cls=EmployeeEncoder))
