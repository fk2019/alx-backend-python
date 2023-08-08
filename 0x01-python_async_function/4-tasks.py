#!/usr/bin/env python3
"""Call task_wait_random
"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of all delays in order"""
    delays: List[float] = []
    complete_delays: List[float] = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    # return awaitable objects in delays list concurrently
    for coro in asyncio.as_completed(delays):
        earliest_result = await coro
        complete_delays.append(earliest_result)
    return complete_delays
