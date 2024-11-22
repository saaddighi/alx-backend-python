
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.perf_counter()
    
    asyncio.run(wait_n(n, max_delay))
    
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
