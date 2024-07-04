#!/usr/bin/env python3
"""
Make a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplier: float number
    return: Function that multiplies
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
