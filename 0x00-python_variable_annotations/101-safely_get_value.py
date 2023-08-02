#!/usr/bin/env python3
"""More type annotations using typevar and mapping
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """Return dct value of default"""
    if key in dict:
        return dct[key]
    else:
        return default
