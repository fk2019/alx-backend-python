#!/usr/bin/env python3
"""async_comprehension: collect and return a list of 10 random
   numbers using async
   comprehension
"""
from typing import List
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return 10 random numbers"""
    result = [i async for i in async_generator()]
    return result
