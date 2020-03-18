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
        self.assertTrue(args.foo)

    def test_empty_list(self):
        sys.argv = ["thecastleargv"]
        parser = argparse.ArgumentParser()
        parser.add_argument('--foo', action='append', default=[])
        args = parser.parse_args()
        self.assertEqual(args.foo, [])

    def test_list(self):
        sys.argv = ["thecastleargv", "--foo=bar", "--foo=baz"]
        parser = argparse.ArgumentParser()
        parser.add_argument('--foo', action='append')
        args = parser.parse_args()
        self.assertTrue('bar' in args.foo)
        self.assertTrue('baz' in args.foo)
