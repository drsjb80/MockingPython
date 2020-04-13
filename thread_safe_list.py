import threading
import unittest

class ThreadSafeList():
    def __init__(self):
        self.list = []
        self.lock = threading.Lock()

    def append(self, element):
        self.lock.acquire()
        self.list.append(element)
        self.lock.release()

    def extend(self, elements):
        self.lock.acquire()
        self.list.extend(elements)
        self.lock.release()

    def rotate(self):
        self.lock.acquire()
        ret = self.list.pop()
        self.list.insert(0, ret)
        self.lock.release()
        return ret

    def clear(self):
        self.lock.acquire()
        self.list.clear()
        self.lock.release()

class TestThreadSafeList(unittest.TestCase):
    def test_empty(self):
        a = ThreadSafeList()
        self.assertEqual(len(a.list), 0)
        self.assertEqual(a.list, [])

    def test_append(self):
        a = ThreadSafeList()
        a.append('foo')
        self.assertEqual(len(a.list), 1)
        self.assertEqual(a.list, ['foo'])

    def test_extend(self):
        a = ThreadSafeList()
        a.extend(['foo', 'bar'])
        self.assertEqual(len(a.list), 2)
        self.assertEqual(a.list, ['foo', 'bar'])

    def test_rotate(self):
        a = ThreadSafeList()
        a.extend(['foo', 'bar'])
        r = a.rotate()
        self.assertEqual(r, 'bar')
        self.assertEqual(a.list, ['bar', 'foo'])

    def test_clear(self):
        a = ThreadSafeList()
        a.extend(['foo', 'bar'])
        self.assertEqual(len(a.list), 2)
        self.assertEqual(a.list, ['foo', 'bar'])
        a.clear()
        self.assertEqual(len(a.list), 0)
        self.assertEqual(a.list, [])
