#!/usr/bin/env python3
"""wait_random coroutine waits for random delay and return result
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """wait for random delay"""
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
