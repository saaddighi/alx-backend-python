#!/usr/bin/env python3

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that takes a list mxd_lst of integers 
and floats and returns their sum as a float."""
    sum = 0
    for i in mxd_lst:
        sum = sum + i
    return float(sum)
