import pdb
import random
import unittest
from collections import Iterable
from functools import total_ordering


def index_check(length, index):
    if index > length:
        raise IndexError("list index out of range")


@total_ordering
class SingleLinkNode:
    def __init__(self, value=None, next_node=None):
        self._value = value
        self.next_node = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if self.value == other:
            return True

    def __lt__(self, other):
        if self.value < other:
            return True


class DoubleLinkNode(SingleLinkNode):
    def __init__(self, value=None):
        self.previous = None
        super(DoubleLinkNode, self).__init__(value)

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, previous):
        self._previous = previous


class SingleLinkedList:
    """
    A single linked list. All operations should be O(n) or O(1). Utilizes
    merge-sort, O(nlogn).
    """
    def __init__(self):
        self.head = SingleLinkNode()

    def append(self, value: object):
        new_node = DoubleLinkNode(value)
        if len(self) == 0:
            self.head = new_node
        else:
            index = 0
            current_node = self.head
            while index < len(self)-1:
                current_node = current_node.next_node
                index += 1
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def extend(self, items: Iterable):
        for item in items:
            self.append(item)

    def insert(self, index: int, value: object):
        new_node = SingleLinkNode(value)
        index_check(len(self), index)
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

    def pop(self, index: int=0):
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
        if self.head is None:
            return count
        current_node = self.head
        if current_node.value is None:
            return count
        while current_node is not None:
            current_node = current_node.next_node
            count += 1
        return count

    def __getitem__(self, index: int):
        if index >= len(self):
            raise IndexError("list index out of range")
        if index < 0:
            index %= len(self)
        current_node = self.head
        while index:
            current_node = current_node.next_node
            index -= 1

        return current_node

    def __setitem__(self, index: int, value: object):
        new_node = SingleLinkNode(value)
        if index >= len(self):
            raise IndexError("list index out of range")
        if index < 0:
            index %= len(self)
        if index == 0:
            new_node.next_node = self.head.next_node
            self.head = new_node
        else:
            i = 0
            current_node = self.head
            while i < index:
                current_node = current_node.next_node
                i += 1
            new_node.next_node = current_node.next_node
            if current_node.next_node:
                current_node.next_node.previous = new_node

    def __delitem__(self, index: int):
        if index < 0:
            index %= len(self)
        if index >= len(self):
            raise IndexError("list index out of range")
        if index == 0:
            self.head = self.head.next_node
        else:
            i = 0
            current_node = self.head
            while i < index-1:
                current_node = current_node.next_node
                i += 1
            current_node.next_node = current_node.next_node.next_node

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


class DoubleLinkedList:
    def __init__(self):
        """
        A double linked list.
        Sort: O(nlogn)
        Insert: O(1) best O(n) worse

        """
        self.head = DoubleLinkNode()

    def append(self, value: object):
        new_node = DoubleLinkNode(value)
        if len(self) == 0:
            self.head = new_node
        else:
            index = 0
            current_node = self.head
            while index < len(self)-1:
                current_node = current_node.next_node
                index += 1
            new_node.next_node = current_node.next_node
            new_node.previous = current_node
            current_node.next_node = new_node

    def extend(self, items: Iterable):
        for item in items:
            self.append(item)

    def insert(self, index: int, value: object):
        new_node = DoubleLinkNode(value)
        index_check(len(self), index)
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
            new_node.previous = current_node
            current_node.next_node = new_node

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

    def remove(self, value: object):
        if value not in self:
            raise ValueError("list.remove(x): x not in list")
        current_node = self.head
        index = 0
        while current_node != value:
            current_node = current_node.next_node
            index += 1
        self.__delitem__(index)

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

    def __len__(self):
        count = 0
        if self.head is None:
            return count
        current_node = self.head
        if current_node.value is None:
            return count
        while current_node is not None:
            current_node = current_node.next_node
            count += 1
        return count

    def __getitem__(self, index: int):
        if index >= len(self):
            raise IndexError("list index out of range")
        if index < 0:
            index %= len(self)
        current_node = self.head
        while index:
            current_node = current_node.next_node
            index -= 1
        return current_node

    def __setitem__(self, index: int, value: object):
        new_node = DoubleLinkNode(value)
        if index >= len(self):
            raise IndexError("list index out of range")
        if index < 0:
            index %= len(self)
        if index == 0:
            new_node.next_node = self.head.next_node
            self.head = new_node
        else:
            i = 0
            current_node = self.head
            while i < index:
                current_node = current_node.next_node
                i += 1
            next_item = current_node.next_node
            previous_node = current_node.previous
            new_node.next_node = next_item
            new_node.previous = previous_node
            if previous_node:
                previous_node.next_node = new_node
            if next_item:
                next_item.previous = new_node

    def __delitem__(self, index: int):
        if index < 0:
            index %= len(self)
        if index >= len(self):
            raise IndexError("list index out of range")
        if index == 0:
            self.head = self.head.next_node
        else:
            i = 0
            current_node = self.head
            while i < index:
                current_node = current_node.next_node
                i += 1
            current_node.previous.next_node = current_node.next_node
            if current_node.next_node:
                current_node.next_node.previous = current_node.previous

    def __iter__(self):
        front_node = self.head
        while front_node:
            yield front_node
            front_node = front_node.next_node


class TestDoubleLinkedList(unittest.TestCase):

    def test_append(self):
        test_list = DoubleLinkedList()
        test_list.append("TEST")
        test_list.append("Next")
        self.assertEqual("TEST", test_list[0])

    def test_extend(self):
        test_list = DoubleLinkedList()
        test_list.extend(range(5))
        self.assertListEqual(list(range(5)), list(test_list))

    def test_insert(self):
        test_list = DoubleLinkedList()
        test_list.extend(range(5))
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
        tst[3] = 0

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
        tst[3] = 0

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
