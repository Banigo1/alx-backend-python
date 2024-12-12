#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    
    @parameterized.expand([
        ("single_key", {"a": 1}, ("a",), 1),
        ("nested_key", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("deep_nested_key", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    unittest.main()
