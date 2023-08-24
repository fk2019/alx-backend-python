#!/usr/bin/env python3
"""A module for parametarizing a unit test
"""
import unittest
from parameterized import parameterized
from typing import (
    Dict,
    Mapping,
    Sequence,
    Union,
)
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected_result: Union[Dict, int]
            ) -> None:
        """Tests access_nested_map's output"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            exception: Exception) -> None:
        """Tests access_nested_map's output for exception"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
