#!/usr/bin/env python3

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a function that hat takes a string k and an int
    OR float v as arguments and returns a tuple"""
    tup = k, float(v*v)
    return tuple(tup)
