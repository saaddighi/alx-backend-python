#!/usr/bin/env python3

import asyncio
"""asyncio module to await the task"""
import random
"""random module to randomly generate the delay time"""


async def wait_random(max_delay: int = 10) -> float:
    """ Generate a random float between 0 and max_delay """
    sleeptime = random.uniform(0, max_delay)
    """ Wait for the generated delay time """
    await asyncio.sleep(sleeptime)
    return sleeptime
