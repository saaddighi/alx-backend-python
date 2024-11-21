#!/usr/bin/env python3

import asyncio
from typing import List
import bisect


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    res = []
    for i in range(0, n):
        wait_random(max_delay)
        res.append(max_delay)
    sorted_list = []
    for element in res:
        bisect.insort(sorted_list, element)

    return sorted_list
