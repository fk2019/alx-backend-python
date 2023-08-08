#!/usr/bin/env python3
"""async_generator: loop 10 times yielding 0-10
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Yield 0-10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.random() * 10)
