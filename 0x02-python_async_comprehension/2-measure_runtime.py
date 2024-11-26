#!/usr/bin/env python3

import asyncio
import random
from typing import Generator, List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """a courotine that oroutine that will execute async_comprehension
    four times in parallel using asyncio.gather and returns the runtime"""
    start_time = time.time()
    task = [async_comprehension() for i in range(0, 4)]
    result = await asyncio.gather(*task)
    end_time = time.time()
    return end_time - start_time
