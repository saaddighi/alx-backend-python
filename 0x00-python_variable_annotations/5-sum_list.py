#!/usr/bin/env python3

from typing import List


def sum_list(input_list: List[float])-> float:
    """a function that returns their sum as a float"""
    sum = 0
    for i in input_list:
        sum = sum + i
    return float(sum)
