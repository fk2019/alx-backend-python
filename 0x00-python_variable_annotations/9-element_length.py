#!/usr/bin/env python3
"""Element_length returns a list of tuple of elements and their lengths
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuple"""
    return [(i, len(i)) for i in lst]
