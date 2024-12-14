#!/usr/bin/env python3
""" A script to unit test for uclient.GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from unittest import mock
from unittest.mock import PropertyMock, patch
import requests
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """_class and implement the test_org method.
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """ test that GithubOrgClient.org returns the correct value."""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.called_with_once(test_class.ORG_URL)

    def test_public_repos_url(self):
        """unit-test GithubOrgClient._public_repos_url"""
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_property:
            mock_property.return_value = 'mock_value'
            inst = GithubOrgClient('org_name')

            self.assertEqual(inst._public_repos_url, 'mock_value')


if __name__ == '__main__':
    unittest.main()


# Task 5

    import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient # Replace with your actual module

class TestGithubOrgClient(unittest.TestCase):
    @patch('your_module.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        # Define a known payload
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the method under test
        result = client._public_repos_url()

        # Assert that the result is as expected
        expected_url = "https://api.github.com/orgs/test_org/repos"
        self.assertEqual(result, expected_url)

if __name__ == '__main__':
    unittest.main()


# Task 6

class TestGithubOrgClient(unittest.TestCase):
    @patch('your_module.GithubOrgClient.get_json')
    def test_public_repos(self, mock_get_json):
        # Mock the _public_repos_url method using a context manager
        with patch('your_module.GithubOrgClient._public_repos_url', return_value="https://api.github.com/orgs/test_org/repos"):
            # Define a known payload to be returned by get_json
            mock_get_json.return_value = [
                {"name": "repo1", "url": "https://github.com/test_org/repo1"},
                {"name": "repo2", "url": "https://github.com/test_org/repo2"}
            ]

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test_org")

            # Call the public_repos method
            repos = client.public_repos()

            # Expected list of repositories
            expected_repos = [
                {"name": "repo1", "url": "https://github.com/test_org/repo1"},
                {"name": "repo2", "url": "https://github.com/test_org/repo2"}
            ]

            # Assert that the returned list matches the expected list
            self.assertEqual(repos, expected_repos)

            # Assert that get_json was called once
            mock_get_json.assert_called_once()

# Run the tests
if __name__ == '__main__':
    unittest.main()

# Task 7
    class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the has_license method
        result = client.has_license(repo, license_key)

        # Assert that the result matches the expected value
        self.assertEqual(result, expected)

# Run the tests
if __name__ == '__main__':
    unittest.main()