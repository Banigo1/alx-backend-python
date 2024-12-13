#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from typing import Dict

def get_json(url: str) -> Dict:
    """Get JSON from remote URL."""
    response = requests.get(url)
    return response.json()

class TestGetJson(unittest.TestCase):

    @patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        # Setup the mock to return a response with the test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        # Call the function with the test_url
        result = get_json(test_url)
        
        # Assert the mock was called once with the test_url
        mock_get.assert_called_once_with(test_url)
        
        # Assert the function's output matches the test_payload
        self.assertEqual(result, test_payload)

if __name__ == '__main__':
    unittest.main()
