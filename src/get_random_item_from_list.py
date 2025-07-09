from random import randint
from typing import List, TypeVar


T = TypeVar("T")


def get_random_item_from_list(a: List[T]) -> T:
    """
    Gets random item from the list and returns it.
    """
    return a[randint(0, len(a) - 1)]
