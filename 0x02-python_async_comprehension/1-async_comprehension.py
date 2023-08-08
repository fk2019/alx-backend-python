#!/usr/bin/env python3
"""async_comprehension: collect and return 10 random numbers using async
 comprehension
"""
from typing import Generator
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """return 10 random numbers"""
    result = [i async for i in async_generator()]
    return result
