#!/usr/bin/env python3
"""
Fix it
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Getting fixed ...
    """
    return [(i, len(i)) for i in lst]
