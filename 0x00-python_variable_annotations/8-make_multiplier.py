#!/usr/bin/env python3
"""make_multiplier returns function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies multiplier"""
    def multiply(multiplier: float) -> float:
        """multiply multiplier"""
        return multiplier ** 2
    return multiply
