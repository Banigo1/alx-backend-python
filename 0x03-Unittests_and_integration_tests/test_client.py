#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized
from github_org_client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
        ("google", {"name": "google", "repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"name": "abc", "repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch("github_org_client.get_json")
    def test_org(self, org_name, expected_org, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        # Mock the return value of get_json
        mock_get_json.return_value = expected_org

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org property
        result = client.org

        # Assert get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert the result matches the expected organization data
        self.assertEqual(result, expected_org)

if __name__ == "__main__":
    unittest.main()
