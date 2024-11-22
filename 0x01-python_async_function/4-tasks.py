#!/usr/bin/env python3


import asyncio
import bisect
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    res = []
    for i in range(0, n):
        t = await task_wait_random(max_delay)
        res.append(t)
    sorted_list = []
    for element in res:
        bisect.insort(sorted_list, element)

    return sorted_list
