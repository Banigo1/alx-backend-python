#!/usr/bin/env python3

import unittest
from functools import wraps
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        # Test case: Simple key access
        # Test case: Nested dictionary access
        # Test case: Deep nested access
    ])
    def test_access_nested_map(
        self, map: Dict, path: Tuple[
            str], ex: Union[Dict, int]) -> None:
        """Test that access_nested_map returns
        expected results for given inputs.

    Args:
    map (Dict): The nested dictionary to test.
    path (Tuple[str]): The path to access within the nested dictionary.
    ex (Union[Dict, int]): The expected result from accessing the nested map.

        Asserts:
        The function should return the expected
        result based on the input map and path.
        """
        self.assertEqual(access_nested_map(map, path), ex)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        # Test case: Empty map raises KeyError

        ({"a": 1}, ("a", "b"), KeyError),
        # Test case: Valid key but invalid nested key raises KeyError
    ])
    def test_access_nested_map_exception(self, map: Dict, path: Tuple[str], 
    ex: Exception) -> None:
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
