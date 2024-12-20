#!/usr/bin/env python3

"""
test_utils.py

This module contains unit tests for utility functions, specifically for:
- access_nested_map: A function for accessing nested dictionaries.
- memoize: A decorator for caching function results.

The tests are organized into classes that use the unittest framework,
and they utilize parameterized testing to cover various input scenarios.

Usage:
Run this module to execute the unit tests.
"""

import unittest
from functools import wraps
from parameterized import parameterized
from utils import access_nested_map, memoize
from typing import Dict, Tuple, Union
from unittest.mock import patch, MagicMock
import requests

#---------------------Task 0

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected results."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"KeyError: '{path[-1]}'")

if __name__ == "__main__":
    unittest.main()

#---------------------Task 1

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        # Additional test cases can be added here.
    ])
    def test_access_nested_map(
        self, map: Dict, path: Tuple[str], ex: Union[Dict, int]
    ) -> None:
        """Test that access_nested_map
        returns expected results for valid inputs.

        Args:
            map (Dict): The nested dictionary to test.
            path (Tuple[str]): The path to
            access within the nested dictionary.
            ex (Union[Dict, int]):
            The expected result from accessing the nested map.

        Asserts:
            The function should return the
            expected result based on the input map and path.
        """
        self.assertEqual(access_nested_map(map, path), ex)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        # Additional test cases can be added here.
    ])
    def test_access_nested_map_exception(
        self, map: Dict, path: Tuple[str], ex: Exception
    ) -> None:
        """Test that KeyError is raised for invalid paths.

        Args:
            map (Dict): The nested dictionary to test.
            path (Tuple[str]): The path to access within the nested dictionary.
            ex (Exception): The expected exception type to be raised.

        Asserts:
            A KeyError should be raised when
            accessing an invalid path in the nested map.
        """
        with self.assertRaises(ex):
            access_nested_map(map, path)


def memoize(func):
    """A decorator that caches the results of a function call.

    This decorator stores previously computed results of a function in a cache,
    allowing for faster retrieval on subsequent calls with the same arguments.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: A wrapper function that implements memoization.
    """
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


class TestClass:
    """A class containing methods for testing memoization."""

    def a_method(self):
        """Returns a constant value of 42."""
        return 42

    @memoize
    def a_property(self):
        """Returns the result of a_method, cached by memoization."""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """Test that a_property returns correct value and calls a_method once.

        This method tests that when calling a_property twice,
        it returns the correct result but only calls a_method once,
        demonstrating effective caching.

        Args:
            mock_a_method (Mock): The mocked version of a_method.

        Asserts:
            The results from two calls to a_property should be equal to 42,
            and a_method should only be called once.
        """
        obj = TestClass()

        # Call a_property twice
        result1 = obj.a_property()
        result2 = obj.a_property()

        # Check that the result is correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        # Ensure a_method was only called once
        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()

#---------------------Task 2

def get_json(url: str) -> Dict:
    """Get JSON from remote URL."""
    response = requests.get(url)
    return response.json()

class TestGetJson(unittest.TestCase):
    
    @patch('requests.get')
def test_get_json(self, mock_get):
        # Define test cases
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
        
    for test_url, test_payload in test_cases:
            # Set up the mock to return a specific payload
            mock_response = MagicMock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            
            # Call the function with the test URL
            result = get_json(test_url)
            
            # Assert that the mocked get method was called with the correct URL
            mock_get.assert_called_once_with(test_url)
            
            # Assert that the result matches the expected payload
            self.assertEqual(result, test_payload)

            # Reset the mock for the next iteration
            mock_get.reset_mock()

if __name__ == "__main__":
    unittest.main()
