#!/usr/bin/env python3

import unittest
from parameterized import parameterized

def access_nested_map(nested_map, path):
    """
    Access a value in a nested dictionary using a tuple as a path.

    Args:
        nested_map (dict): The nested dictionary to access.
        path (tuple): A tuple of keys that represent the path to the desired value.

    Returns:
        The value located at the specified path in the nested dictionary.

    Raises:
        KeyError: If any key in the path does not exist in the nested_map.
    """
    for key in path:
        # Access each key in the path to drill down into the nested dictionary
        nested_map = nested_map[key]
    return nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test class for testing the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),                      # Test case 1: Simple access
        ({"a": {"b": 2}}, ("a",), {"b": 2}),      # Test case 2: Accessing a nested dictionary
        ({"a": {"b": 2}}, ("a", "b"), 2),         # Test case 3: Accessing a deeper level
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function with various inputs.

        Args:
            nested_map (dict): The nested dictionary to test.
            path (tuple): The path to access within the nested dictionary.
            expected: The expected result of accessing the path.

        Asserts:
            The output of access_nested_map matches the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    # Run the unit tests when this script is executed directly
    unittest.main()
