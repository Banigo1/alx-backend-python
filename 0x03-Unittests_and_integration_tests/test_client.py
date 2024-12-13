#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from requests import Response  # Import Response for clarity

def get_json(url: str) -> Dict:
  """Get JSON from remote URL.

  Args:
      url: The URL to fetch JSON data from.

  Returns:
      A dictionary containing the parsed JSON data, or raises an exception on error.
  """
  response = requests.get(url)
  response.raise_for_status()  # Raise exception for non-2xx status codes
  return response.json()

class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')  # Patch requests.get from the 'utils' module
    def test_get_json(self, mock_get):
        test_data = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_data:
            # Configure the mock to return a Response object with the desired JSON
            mock_response = Response()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function under test
            result = get_json(test_url)

            # Assertions
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)

if __name__ == '__main__':
    unittest.main()