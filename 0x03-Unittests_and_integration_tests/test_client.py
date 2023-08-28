#!/usr/bin/env python3
import unittest
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""
    @parameterized.expand([
        ('google',),
        ('abc', )
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get: MagicMock) -> None:
        """test method for org method"""
        expected = {'login': org}
        mock_get.return_value = expected
        client = GithubOrgClient(org)
        res = client.org
        self.assertEqual(res, expected)
        mock_get.assert_called_once_with(client.ORG_URL.format(
            org=org))

    @parameterized.expand([
        ('google', {'repos_url': 'https://api.github.com/orgs/google/repos'})
    ])
    def test_public_repos_url(self, org: str, expected: Dict) -> None:
        """Test public_repos_url property"""
        with patch('client.GithubOrgClient._public_repos_url') as mock_repo:
            mock_repo.return_value = expected
            client = GithubOrgClient(org)
            res = client._public_repos_url()
            self.assertEqual(res, expected)

    @parameterized.expand([
        ('google', ['truth', 'autoparse'])
    ])
    @patch('client.get_json')
    def test_public_repos(self, org: str, expected: list,
                          mock_get: MagicMock) -> None:
        """Test public repos method using patch as decorator and context
        manager"""
        mock_get.return_value = [{'name': 'truth'}, {'name': 'autoparse'}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'https://api.github.com/orgs/google/repos'
            client = GithubOrgClient(org)
            res = client.public_repos()
            self.assertEqual(res, expected)
            mock_url.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str,
                         expected: bool) -> None:
        """Test the has_license method"""
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for client and only mock code that
    sends external requests. """
    @classmethod
    def setUpClass(cls):
        """the setup class """
        conf = {'return_value.json.side_effect':
                [cls.org_payload, cls.repos_payload,
                 cls.org_payload, cls.repos_payload]}
        cls.get_patcher = patch('requests.get', **conf)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """the teardown method """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test the public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("VAGUELICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public.repos method with with the argument
        license="apache-2.0" """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.mock.assert_called()
