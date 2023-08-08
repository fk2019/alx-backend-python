#!/usr/bin/env python3
"""measure_time: measures the execution time
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure run time of delays"""
    start_t = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_t
    return total_time / n
