"""

    This code runs without error.  But using improper values in the
    functions and methods will cause the items to be highlighted in the IDE.

"""
from typing import Tuple, Any, Union, Optional

Fullname = tuple[str, str]                              # this is a type alias


def display_info(name: Fullname, nickname: Any, age: int, spouse: str,
                 children: list,
                 parents: Tuple,
                 children_ages: list[Union[str, int]],
                 parent_ages: list[str | int],
                 other_family: Optional = None) -> dict:
    return display_info.__annotations__


print(display_info(('John', 'Smith'), 'Johnny', 40, 'Sally', ['Tim', 'Sam'],
                   parents=('Martha', 'Frank'),
                   children_ages=['22', 10],
                   parent_ages=[65, '70']))
