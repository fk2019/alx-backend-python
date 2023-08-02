#!/usr/bin/env python3
"""sum_mixed_list returns sum of mxd_list and return as flaot
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return sum of list items"""
    return sum(mxd_list)
