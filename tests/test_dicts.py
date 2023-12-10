import unittest
from utils import dicts


class TestDict(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({'hello': 'world'}, 'hello', 'Empty'), 'world')
        self.assertEqual(dicts.get_val({'hello': 'world'}, '', 'Empty'), 'Empty')
        self.assertEqual(dicts.get_val({'hello': 'world'}, None, 'Empty'), 'Empty')
        self.assertEqual(dicts.get_val({1: 'one', 2: 'two'}, '2', 'Empty'), 'Empty')
        self.assertEqual(dicts.get_val({'1': 'one', '2': 'two'}, 2, 'Empty'), 'Empty')
        self.assertEqual(dicts.get_val({}, 2, 'Empty'), 'Empty')
        self.assertEqual(dicts.get_val(None, 2, 'Empty'), 'Empty')
        self.assertEqual(dicts.get_val({1: 'one', 2: 'two'}, 2, 'Empty'), 'two')
