#!/usr/bin/python
import unittest
from parser import parse

class ParserTest(unittest.TestCase):

    def test_day(self):
        self.assertEqual(parse('1D'), 86400)
        self.assertEqual(parse('12d'), 1036800)
    
    def test_hour(self):
        self.assertEqual(parse('..1H'), 3600)
        self.assertEqual(parse('..2h'), 7200)

    def test_minute(self):
        self.assertEqual(parse('1m'), 60)
        self.assertEqual(parse('10M'), 600)

    def test_second(self):
        self.assertEqual(parse('1S'), 1)
        self.assertEqual(parse('500s'), 500)

if __name__ == '__main__':
    unittest.main()
