#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and its length.
    
    :param lst: Iterable of sequences
    :return: List of tuples, each containing a sequence and its length
    """
    return [(i, len(i)) for i in lst]
