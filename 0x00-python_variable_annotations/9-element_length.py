#!/usr/bin/env python3

from typing import List

def element_length(lst: List[int]) -> List[int]:
    return [(i, len(i)) for i in lst]
