import random
import unittest
from typing import Iterable

from DataStructures.nodes import SingleLinkNode


class SingleLinkedList:
    """
    A single linked list. All operations should be O(n) or O(1). Utilizes
    merge-sort, O(nlogn).
    """

    def __init__(self):
        self.head = SingleLinkNode()

    def get_node(self, index):
        i = 0
        current_node = self.head
        while i < index:
            current_node = current_node.next_node
            i += 1
        return current_node

    def out_of_range(self, index):
        if index >= len(self):
            raise IndexError("list index out of range")

    def neg_index(self, index):
        if index < 0:
            index %= len(self)
        return index

    def append(self, value: object):
        new_node = SingleLinkNode(value)
        if len(self) == 0:
            self.head = new_node
        else:
            index = 0
            current_node = self.head
            while index < len(self) - 1:
                current_node = current_node.next_node
                index += 1
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def extend(self, items: Iterable):
        for item in items:
            self.append(item)

    def insert(self, index: int, value: object):
        new_node = SingleLinkNode(value)
        self.out_of_range(index)
        if index == 0:
            new_node.next_node = self.head.next_node
            self.head = new_node
        if index < 0:
            index %= len(self)
        else:
            current_node = self.head
            while index > 1:
                current_node = current_node.next_node
                index -= 1
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def pop(self, index: int = 0):
        item = self.__getitem__(index)
        self.__delitem__(index)
        return item

    def remove(self, value: object):
        current_node = self.head.next_node
        index = 0
        while current_node != value:
            current_node = current_node.next_node
            index += 1
        self.__delitem__(index)

    def _split(self):
        right_list = SingleLinkedList()
        if len(self) <= 1:
            return None
        else:
            mid_point = self.head
            front_runner = self.head.next_node
            while front_runner:
                front_runner = front_runner.next_node

                if front_runner:
                    mid_point = mid_point.next_node
                    front_runner = front_runner.next_node
            right_list.head = mid_point.next_node
            mid_point.next_node = None
            return right_list

    def _merge(self, list2):
        fake_list = SingleLinkedList()
        current_node = fake_list.head
        left_node = self.head
        right_node = list2.head
        while left_node and right_node:
            if left_node <= right_node:
                current_node.next_node = left_node
                left_node = left_node.next_node
            else:
                current_node.next_node = right_node
                right_node = right_node.next_node
            current_node = current_node.next_node

        if left_node is None:
            while right_node:
                current_node.next_node = right_node
                right_node = right_node.next_node
                current_node = current_node.next_node
        elif right_node is None:
            while left_node:
                current_node.next_node = left_node
                left_node = left_node.next_node
                current_node = current_node.next_node
        self.head = fake_list.head.next_node
        return self

    def sort(self):
        if len(self) <= 1:
            return self
        right = self._split()
        self.sort()
        right_half = right.sort()
        return self._merge(right_half)

    def reverse(self):
        self.__reversed__()

    def __repr__(self):
        return str(list(self))

    def __len__(self):
        count = 0
        # Empty
        if self.head is None:
            return count
        current_node = self.head
        # Head Pointer
        if current_node.value is None:
            return count
        while current_node is not None:
            current_node = current_node.next_node
            count += 1
        return count

    def __getitem__(self, index: int):
        self.out_of_range(index)
        index = self.neg_index(index)
        return self.get_node(index)

    def __setitem__(self, index: int, value: object):
        self.out_of_range(index)
        index = self.neg_index(index)
        new_node = SingleLinkNode(value)
        current_node = self.get_node(index)
        new_node.next_node = current_node.next_node
        if index > 0:
            prev = self.get_node(index - 1)
            prev.next_node = new_node
        elif index == 0:
            self.head = new_node

    def __delitem__(self, index: int):
        self.out_of_range(index)
        index = self.neg_index(index)
        prev = self.get_node(index-1)
        current_node = self.get_node(index)
        prev.next_node = current_node.next_node
        if index == 0:
            self.head = current_node.next_node

    def __reversed__(self):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next_node


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        test_list = SingleLinkedList()
        test_list.append("TEST")
        self.assertTrue("TEST" in test_list)

    def test_extend(self):
        test_list = SingleLinkedList()
        test_list.extend(range(5))
        self.assertEqual(len(range(5)), len(test_list))

    def test_reverse(self):
        test_list = SingleLinkedList()
        test_list.extend(range(6))
        test_list.reverse()
        self.assertListEqual(list(reversed(range(6))), list(test_list))

    def test_split(self):
        test_list = SingleLinkedList()
        test_list.extend(range(6))
        right_list = test_list._split()
        self.assertListEqual(list(range(3)), list(test_list))
        self.assertListEqual(list(range(3, 6)), list(right_list))

    def test_merge(self):
        list1 = SingleLinkedList()
        list1.extend(range(5))
        list2 = SingleLinkedList()
        list2.extend(range(5, 10))
        list1._merge(list2)
        self.assertListEqual(list(range(10)), list(list1))

    def test_sort(self):
        test_list = SingleLinkedList()
        test_list.extend(random.sample(range(6), 6))
        test_list.sort()
        self.assertListEqual(list(range(6)), list(test_list))

    def test_repr(self):
        test_list = SingleLinkedList()
        [test_list.append(i) for i in range(5)]
        self.assertEqual(repr(list(range(5))), repr(test_list))

    def test_len(self):
        empty_test = SingleLinkedList()
        self.assertEqual(0, len(empty_test))
        test_list = SingleLinkedList()
        [test_list.append(i) for i in range(5)]
        self.assertEqual(5, len(test_list))

    def test_getitem(self):
        test_list = SingleLinkedList()
        [test_list.append(i) for i in range(5)]
        self.assertEqual(2, test_list[2])

    def test_pop(self):
        test_list = SingleLinkedList()
        [test_list.append(i) for i in range(5)]
        self.assertEqual(4, test_list.pop(len(test_list)-1))
        self.assertEqual(2, test_list.pop(2))
        self.assertEqual(0, test_list.pop())
        self.assertEqual(3, test_list[1])

    def test_insert(self):
        test_list = SingleLinkedList()
        [test_list.append(i) for i in range(5)]
        test_list.insert(2, "string")
        self.assertEqual("string", test_list[2])

    def test_get(self):
        tst = SingleLinkedList()
        with self.assertRaises(IndexError) as cm:
            tst[0]
        index_except = cm.exception
        self.assertEqual(IndexError, type(index_except))
        tst.extend(range(5))
        self.assertEqual(0, tst[0])
        self.assertEqual(1, tst[1])
        self.assertEqual(3, tst[3])

    def test_set(self):
        tst = SingleLinkedList()
        tst.extend(range(5))
        tst[0] = 5
        self.assertEqual(5, tst[0])
        tst[-1] = 0
        self.assertEqual(0, tst[-1])

    def test_del(self):
        tst = SingleLinkedList()
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
