#!/usr/bin/env python3
"""
Task 1

Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual that the function returns the expected result.

The body of the test method should not be longer than 2 lines.

"""
#!/usr/bin/env python3
""" create class TestAccessNestedMap """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ try test with utils.access_nested_map """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               map: Dict,
                               path: Tuple[str],
                               ex: Union[Dict, int]) -> None:
        """ test nested map """
        self.assertEqual(access_nested_map(map, path), ex)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a", 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         map: Dict,
                                         path: Tuple[str],
                                         ex: Exception) -> None:
        """ test nested loop with exception """
        with self.assertRaises(ex):
            access_nested_map(map, path)




"""
Task 2

Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):

nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
Also make sure that the exception message is as expected.

"""

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({}, ("a",)),  # Test case 1: Empty map, invalid key
        ({"a": 1}, ("a", "b")),  # Test case 2: Valid key at first level, invalid nested key
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


        """
        Task 3
        
        Read about memoization and familiarize yourself with 
        the utils.memoize decorator.

        Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.
         
        Inside test_memoize, define following class

    class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()

    Use unittest.mock.patch to mock a_method.

    Test that when calling a_property twice, the correct result is returned 
    but a_method is only called once using assert_called_once.
        
        """

import unittest
from unittest.mock import patch
from functools import wraps

def memoize(func):
    """A decorator that caches the results of a function call."""
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

class TestClass:
    """
        TestClass: Contains two methods:
            a_method: Returns a constant value (42).
            a_property: Decorated with @memoize, which means it will cache results from calling a_method.
    """
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()

class TestMemoize(unittest.TestCase):
    """
        TestMemoize Class:
        
Inherits from unittest.TestCase.
The test_memoize method uses unittest.mock.patch.object to mock a_method. 
This allows you to control its behavior during testing.
The method calls a_property twice and asserts that it returns the correct value.
Finally, it checks that a_method was called only once using assert_called_once

    """
    
    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
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
