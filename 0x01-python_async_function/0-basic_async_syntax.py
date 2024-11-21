#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int=10):
    sleeptime: float = random(0, max_delay)
    await asyncio.sleep(sleeptime)
    return sleeptime
