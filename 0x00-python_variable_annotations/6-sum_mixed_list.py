#!/usr/bin/env python3
"""
Int and Floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    mxd_lst: mixed list of integers and float numbers
    return: their sum
    """
    return sum(mxd_lst)
