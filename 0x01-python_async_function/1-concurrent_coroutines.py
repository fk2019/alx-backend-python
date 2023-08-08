#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of all delays in order"""
    delays: List[float] = []
    complete_delays: List[float] = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    # return awaitable objects in delays list concurrently
    for coro in asyncio.as_completed(delays):
        earliest_result = await coro
        complete_delays.append(earliest_result)
    return complete_delays
