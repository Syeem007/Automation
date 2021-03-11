import unittest
from regex import rearrange_name


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        tesrcase='lovelac,Ada'
        expected='Ada lovelac'
        self.assertEqual(rearrange_name(tesrcase),expected)


unittest.main()
