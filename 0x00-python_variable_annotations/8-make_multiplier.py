#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float],float]:
    """a function that takes a float multiplier as argument and returns a
    function that multiplies a float by multiplier."""
    def multi(val: float) -> float:
        return val * multiplier
    return multi
