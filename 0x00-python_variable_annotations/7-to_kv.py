#!/usr/bin/env python3
"""
Int or Float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    k: string
    v: into or float
    return: tuple
    """
    sqrd = v**2
    return (k, sqrd)
