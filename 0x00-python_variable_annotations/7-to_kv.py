#!/usr/bin/env python3
"""to_kv returns a tuple from a string and int/float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """Return tuple of string and float"""
    return (k, v ** 2)
