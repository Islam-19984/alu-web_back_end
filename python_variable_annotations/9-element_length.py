#!/usr/bin/env python3
from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes a list of strings and returns a list of tuples,
    where each tuple contains a string and its length.

    :param lst: List of strings
    :return: List of tuples, each containing a string and its length
    """
    return [(i, len(i)) for i in lst]
