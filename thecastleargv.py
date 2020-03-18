# https://docs.python.org/3.3/library/argparse.html

import argparse
import sys
import unittest

class TestArgs(unittest.TestCase):
    def test_help(self):
        sys.argv = ["thecastleargv", "--foo"]
        parser = argparse.ArgumentParser()
        parser.add_argument('--foo', action='store_true')
        args = parser.parse_args()

        self.assertTrue('foo' in args)
        self.assertFalse('bar' in args)
        self.assertEqual(args.foo, True)
