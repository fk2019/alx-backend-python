#!/usr/bin/env python3
"""make_multiplier returns function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies multiplier"""
    return lambda x: x * multiplier
