import pdb
import random
import unittest
from collections import Iterable
from functools import total_ordering

from DataStructures.nodes import DoubleLinkNode
from DataStructures.singlelinkedlist import SingleLinkedList


class DoubleLinkedList(SingleLinkedList):
    def __init__(self):
        """
        A double linked list.
        Sort: O(nlogn)
        Insert: O(1) best O(n) worse
        """
        super(DoubleLinkedList, self).__init__()
        self.head = DoubleLinkNode()

    def append(self, value: object):
        new_node = DoubleLinkNode(value)
        if len(self) == 0:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        new_node.previous = current_node

    def insert(self, index: int, value: object):
        new_node = DoubleLinkNode(value)
        self.out_of_range(index)
        index = self.neg_index(index)
        current_node = self.get_node(index)
        new_node.next_node = current_node
        new_node.previous = current_node.previous
        if current_node.previous:
            current_node.previous.next_node = new_node
        current_node.previous = new_node
        if index == 0:
            self.head = new_node

    def remove(self, value: object):
        if value not in self:
            raise ValueError("list.remove(x): x not in list")
        current_node = self.head
        index = 0
        while current_node != value:
            current_node = current_node.next_node
            index += 1
        self.__delitem__(index)

    def pop(self, index: int=0):
        value = self.__getitem__(index)
        self.__delitem__(index)
        return value

    def _split(self):
        right_list = DoubleLinkedList()
        if len(self) <= 1:
            return None
        else:
            mid_pointer = self.head
            front_runner = self.head.next_node
            while front_runner:
                front_runner = front_runner.next_node

                if front_runner:
                    front_runner = front_runner.next_node
                    mid_pointer = mid_pointer.next_node

            right_list.head = mid_pointer.next_node
            mid_pointer.next_node = None
            return right_list

    def _merge(self, right_list):
        new_list = DoubleLinkedList()
        new_node = new_list.head
        self_node = self.head
        right_node = right_list.head
        while self_node and right_node:
            if self_node <= right_node:
                new_node.next_node = self_node
                self_node = self_node.next_node
            else:
                new_node.next_node = right_node
                right_node = right_node.next_node
            new_node = new_node.next_node
        if self_node is None:
            while right_node:
                new_node.next_node = right_node
                right_node = right_node.next_node
                new_node = new_node.next_node
        elif right_node is None:
            while self_node:
                new_node.next_node = self_node
                self_node = self_node.next_node
                new_node = new_node.next_node
        self.head = new_list.head.next_node
        return self

    def sort(self):
        if len(self) <= 1:
            return self
        right_list = self._split()
        self.sort()
        right = right_list.sort()
        return self._merge(right)

    def reverse(self):
        self.__reversed__()

    def __repr__(self):
        return str(list(self))

    def __reversed__(self):
        current_node = self.head
        prev_node = current_node.previous
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def __setitem__(self, index: int, value: object):
        current_node = self.__getitem__(index)
        new_node = DoubleLinkNode(value)
        new_node.next_node = current_node.next_node
        if current_node.next_node:
            current_node.next_node.previous = new_node
        new_node.previous = current_node.previous
        if current_node.previous:
            current_node.previous.next_node = new_node
        if index == 0:
            self.head = new_node

    def __delitem__(self, index: int):
        current_node = self.__getitem__(index)
        if current_node.previous:
            current_node.previous.next_node = current_node.next_node
        if current_node.next_node:
            current_node.next_node.previous = current_node.previous
        if index == 0:
            self.head = current_node.next_node


class TestDoubleLinkedList(unittest.TestCase):

    def test_append(self):
        test_list = DoubleLinkedList()
        test_list.append("TEST")
        test_list.append("Next")
        self.assertEqual("TEST", test_list[0])
        self.assertEqual("Next", test_list[1])

    def test_extend(self):
        test_list = DoubleLinkedList()
        test_list.extend(range(5))
        self.assertListEqual(list(range(5)), list(test_list))

    def test_insert(self):
        test_list = DoubleLinkedList()
        test_list.extend(range(5))
        test_list.insert(0, "NOT ZERO")
        self.assertEqual("NOT ZERO", test_list[0])
        test_list.insert(2, "HELLO")
        self.assertEqual("HELLO", test_list[2])

    def test_merge(self):
        list1 = DoubleLinkedList()
        list1.extend(range(5))
        list2 = DoubleLinkedList()
        list2.extend(range(5, 10))
        list1._merge(list2)
        self.assertListEqual(list(range(10)), list(list1))

    def test_pop(self):
        test_list = DoubleLinkedList()
        test_list.extend(range(5))
        pop = test_list.pop(3)
        self.assertListEqual([0, 1, 2, 4], list(test_list))
        self.assertEqual(3, pop)

    def test_remove(self):
        test_list = DoubleLinkedList()
        test_list.extend(range(5))
        test_list.remove(3)
        self.assertListEqual([0, 1, 2, 4], list(test_list))

    def test_split(self):
        test_list = DoubleLinkedList()
        test_list.extend(range(10))
        test_split = test_list._split()
        self.assertListEqual(list(range(5)), list(test_list))
        self.assertListEqual(list(range(5, 10)), list(test_split))

    def test_sort(self):
        test_list = DoubleLinkedList()
        test_list.extend(random.sample(range(5), 5))
        test_list.sort()
        self.assertListEqual(list(range(5)), list(test_list))

    def test_reverse(self):
        test_odd_list = DoubleLinkedList()
        test_odd_list.extend(range(5))
        test_odd_list.reverse()
        test_even_list = DoubleLinkedList()
        test_even_list.extend(range(4))
        test_even_list.reverse()
        self.assertListEqual([3, 2, 1, 0], list(test_even_list))
        self.assertListEqual([4, 3, 2, 1, 0], list(test_odd_list))

    def test_get(self):
        tst = DoubleLinkedList()
        with self.assertRaises(IndexError) as cm:
            tst[0]
        index_except = cm.exception
        self.assertEqual(IndexError, type(index_except))
        tst.extend(range(5))
        self.assertEqual(0, tst[0])
        self.assertEqual(1, tst[1])
        self.assertEqual(3, tst[3])

    def test_set(self):
        tst = DoubleLinkedList()
        tst.extend(range(5))
        tst[0] = 5
        self.assertEqual(5, tst[1].previous)
        self.assertEqual(5, tst[0])
        tst[-1] = 0
        self.assertEqual(0, tst[-1])

    def test_del(self):
        tst = DoubleLinkedList()
        with self.assertRaises(IndexError) as cm:
            tst[0]
        index_except = cm.exception
        self.assertEqual(IndexError, type(index_except))
        tst.append(0)
        del tst[0]
        self.assertEqual(0, len(tst))
        tst.extend(range(5))
        del tst[1]
        self.assertListEqual([0, 2, 3, 4], list(tst))
        del tst[-1]
        self.assertListEqual([0, 2, 3], list(tst))


if __name__ == '__main__':
    unittest.main()
