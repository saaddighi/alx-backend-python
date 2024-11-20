#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a fucntion that takes a list and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
