#!/usr/bin/env python3
"""measure_runtime: Execute async_comprehension 4 times in parallel with
   asyncio.gather
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return total runtime"""
    start_t = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_t
