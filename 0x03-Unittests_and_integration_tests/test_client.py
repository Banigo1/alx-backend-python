import unittest
from unittest.mock import patch, Mock
from typing import Dict
import requests

# Assuming the get_json function is defined in a module named utils
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
            # Set up the mock to return a response with the desired JSON
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            
            # Call the function under test
            result = get_json(test_url)
            
            # Assert that the mocked get method was called once with the correct URL
            mock_get.assert_called_once_with(test_url)
            
            # Assert that the result matches the expected payload
            self.assertEqual(result, test_payload)

            # Reset the mock for the next iteration
            mock_get.reset_mock()

if __name__ == '__main__':
    unittest.main()