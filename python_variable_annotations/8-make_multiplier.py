#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    :param multiplier: The multiplier to use.
    :return: A function that multiplies a float by the multiplier.
    """
    def multiply_by_multiplier(value: float) -> float:
        """Multiplies a float by the stored multiplier."""
        return value * multiplier

    return multiply_by_multiplier