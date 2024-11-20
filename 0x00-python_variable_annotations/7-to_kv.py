#!/usr/bin/env python3


def to_kv(k: str, v: int or float) -> tuple:
    tup = k,float(v*v)
    return tuple(tup)
