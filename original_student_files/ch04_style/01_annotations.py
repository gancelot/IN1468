"""
    01_annotations.py - This code runs without error.  But using improper
                        values in the functions and methods will cause the items
                        to be highlighted in the IDE.
"""
from dataclasses import dataclass
from typing import List, Tuple, Any, Union


def display_info(name: str, age: int, spouse: str, *children: Any,
                 parents: list, **other_family: Union[str, int]) -> dict:
    return display_info.__annotations__


print(display_info('John', 40, 'Sally', 'Tim', 'Sam', 10,
                   parents=['Martha', 'Frank'], sister='Amy'))


# Python 3.6+, variable annotations
my_list: List[int] = [1, 2, 3]
my_list.append('hello')

# this is a type alias
Group = Tuple[str, str, str, str]


@dataclass
class Members:
    names: Group


c = Members(names=('John', 'Paul', 'George', 'Ringo'))
c2 = Members('John')
