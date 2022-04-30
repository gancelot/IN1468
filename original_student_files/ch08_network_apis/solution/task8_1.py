"""
    task8_1.py
"""
import dataclasses
import datetime
import json

import requests

results = []


@dataclasses.dataclass
class Character:
    name: str
    actor: str
    role: str
    original_air_date: datetime.date


char_name = input('Enter partial Simpsons character name: ')
data = requests.get(f'http://localhost:8051/simpsons?char_name={char_name}').json()

for character in data.get('results', []):
    actor = character.get('actor')
    name = character.get('name')
    role = character.get('role')
    date_str = character.get('original_air_date')
    try:
        orig_air_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        orig_air_date = date_str

    results.append(Character(name, actor, role, orig_air_date))


class CharacterEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            result = obj.__dict__
        except (AttributeError, TypeError):
            if isinstance(obj, datetime.date):
                result = obj.strftime('%Y-%b-%d')
            else:
                result = '(unknown type)'
        return result


with open('simpsons_data.json', 'wt') as f:
    json.dump(results, f, cls=CharacterEncoder)
    print('Write complete.  Open file to view results.')
