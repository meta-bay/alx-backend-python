#!/usr/bin/env python3
'''
test utils
'''
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
import utils
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests access nested map"""
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''tests access nested map'''
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''tests if it raises keyerror as it should'''
        with self.assertRaises(expected):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''class to test get_json function'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, req):
        '''tests get_json function'''
        mock = Mock()
        mock.json.return_value = test_payload
        req.return_value = mock
        self.assertEqual(utils.get_json(test_url), test_payload)
        req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """class to mock memoize"""

    def test_memoize(self):
        '''mocks memoize'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as memo:
            memo.return_value = 42
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            memo.assert_called_once()

