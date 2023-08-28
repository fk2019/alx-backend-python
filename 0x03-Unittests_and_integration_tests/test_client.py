#!/usr/bin/env python3
import unittest
from parameterized import parameterized
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
