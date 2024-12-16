#!/usr/bin/env python3
""" A script to unit test for uclient.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized
from unittest import mock
import requests
import client
from github_org_client import GithubOrgClient
from client import GithubOrgClient
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

# -------------------------------------------------Task 4


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
        with patch.object(GithubOrgClient,
        '_public_repos_url',
        new_callable=PropertyMock
        ) as mock_property:
            mock_property.return_value = 'mock_value'
            inst = GithubOrgClient('org_name')

    self.assertEqual(inst._public_repos_url, 'mock_value')


if __name__ == '__main__':
    unittest.main()


#--------------------------------------------------Task 5

class TestGithubOrgClient(unittest.TestCase):
    @patch('your_module.GithubOrgClient.org', new_callable=PropertyMock)


    def test_public_repos_url(self, mock_org):
        # Define a known payload
        mock_org.return_value = {
            "repos_url":
            "https://api.github.com/orgs/test_org/repos"
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the method under test
        result = client._public_repos_url()

        # Assert that the result is as expected
        expected_url =
        "https://api.github.com/orgs/test_org/repos"
        self.assertEqual(result, expected_url)

if __name__ == '__main__':
    unittest.main()


#--------------------------------------------------Task 6


class TestGithubOrgClient(unittest.TestCase):

    """
    Test suite for the GithubOrgClient class.
    This suite tests the functionality
    of the `public_repos` method.

    """

    @patch('client.get_json')


    def test_public_repos(self, mock_get_json):
        """
        Test the `public_repos` method.

        This test verifies that:
        1. The method returns the correct list of
        repository names based on the mocked payload.
        2. The `get_json` function is called once with the correct URL.
        3. The `_public_repos_url` property is accessed once.

        Args:
            mock_get_json (Mock): Mocked `get_json` function.
        """
        # Define the payload and expected result
        mock_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        expected_repos = ['repo1', 'repo2', 'repo3']
        mock_get_json.return_value = mock_payload

        # Mock the _public_repos_url property
        with patch.object(GithubOrgClient,
    '_public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value =
            'https://api.github.com/orgs/test_org/repos'

            # Initialize client and call the method
            client = GithubOrgClient('test_org')
            repos = client.public_repos()

            # Assertions
            self.assertEqual(repos, expected_repos)
            # Test the result matches the expected list
            mock_get_json.assert_called_once_with
            ('https://api.github.com/orgs/test_org/repos')
            mock_url.assert_called_once()
            # Ensure the mocked property was accessed

if __name__ == '__main__':
    unittest.main()

#--------------------------------------------------Task 7

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

#--------------------------------------------------Task 8

@parameterized_class([
    {"org_payload": org_payload,
    "repos_payload": repos_payload,
    "expected_repos": expected_repos,
    "apache2_repos": apache2_repos},
])


class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side effects for different URLs
        cls.mock_get.side_effect = lambda url: {
        'https://api.github.com/orgs/test_org': cls.org_payload,
        'https://api.github.com/orgs/test_org/repos': cls.repos_payload,
        }.get(url, None)

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        
    # Assert that the returned repos match expected repos
        self.assertEqual(repos, self.expected_repos)

if __name__ == '__main__':
    unittest.main()

#--------------------------------------------------Task 9

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

@patch('github_org_client.GithubOrgClient.public_repos')


def test_public_repos(self, mock_public_repos):


"""Test the public_repos method returns expected results."""
# Sample fixture data
expected_repos = [
{"name": "Repo1", "license": {"key": "mit"}},
{"name": "Repo2", "license": {"key": "apache-2.0"}},
]
        
# Setting up the mock to return the expected repos
mock_public_repos.return_value = expected_repos
        
client = GithubOrgClient("org_name")
repos = client.public_repos()
        
# Assert that the returned repos match the expected repos
self.assertEqual(repos, expected_repos)
 
 @patch('github_org_client.GithubOrgClient.public_repos')
def test_public_repos_with_license(self, mock_public_repos):
"""Test public_repos with license filter."""
# Sample fixture data for license filter
expected_repos_with_license = [
{"name": "Repo2", "license": {"key": "apache-2.0"}},
]
        
# Setting up the mock to return repos with a specific license
mock_public_repos.return_value = expected_repos_with_license
        
client = GithubOrgClient("org_name")
repos = client.public_repos(license="apache-2.0")
        
# Assert that the returned repos match the expected repos with license
self.assertEqual(repos, expected_repos_with_license)

if __name__ == '__main__':
    unittest.main()
