#!/usr/bin/python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
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