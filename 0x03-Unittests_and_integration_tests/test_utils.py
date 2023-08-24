#!/usr/bin/env python3
"""A module for parametarizing a unit test
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from typing import (
    Dict,
    Mapping,
    Sequence,
    Union,
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
    )


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


class TestGetJson(unittest.TestCase):
    """Test case for get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Test method for get_json method"""
        with patch("requests.get") as mock_get:
            mock_response = mock_get.return_value
            mock_response.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize method"""
    def test_memoize(self):
        """Test memoize method"""
        class TestClass:
            """Test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method",
                          return_value=lambda: 42,) as memo_func:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_func.assert_called_once()
