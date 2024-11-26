#!/usr/bin/env python3

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """a coroutine loop 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10"""
    for i in range(0, 10):
        await asyncio.sleep(1)
        gen = random.randint(0, 10)
        yield gen
