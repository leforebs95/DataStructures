import unittest
from typing import Iterable

from DataStructures.doublelinkedlist import DoubleLinkedList


class MinListHeap:
    def __init__(self):
        """
        Min heap which uses a double linked list to maintain parent-children
        relationships
        """
        self.items = DoubleLinkedList()

    def __repr__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    @staticmethod
    def get_left_child_index(parent_index):
        return 2 * parent_index + 1

    def get_left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    @staticmethod
    def get_right_child_index(parent_index):
        return 2 * parent_index + 2

    def get_right_child(self, index):
        return self.items[self.get_right_child(index)]

    @staticmethod
    def get_parent_index(child_index):
        return (child_index-1) // 2

    def get_parent(self, index):
        return self.items[self.get_parent_index(index)]

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.items)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.items)

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def swap(self, index_one, index_two):
        self.items[index_one], self.items[index_two] = \
            self.items[index_two], self.items[index_one]

    def peek(self):
        """
        Returns the smallest item from tree
        :return: Smallest value in tree
        """
        return self.items[0]

    def poll(self):
        """
        Removes the smallest item from tree
        :return: Smallest value in tree
        """
        item = self.items[0]
        self.items[0] = self.items[len(self) - 1]
        del self.items[len(self)-1]
        self.heapify_down(0)
        return item

    def add(self, item):
        """
        Add an item to the tree
        :param item: Item to be added
        :return:
        """
        self.items.append(item)
        self.heapify_up(len(self)-1)

    def heapify_up(self, index):
        """
        Move a node up the tree as long as it is less than parent
        :param index: Index of node to heapify up
        :return:
        """
        if self.has_parent(index):
            parent = self.get_parent(index)
            if parent > self.items[index]:
                parent_index = self.get_parent_index(index)
                self.swap(parent_index, index)
                self.heapify_up(parent_index)

    def heapify_down(self, index):
        """
        Move a node down the tree as long as it is greater than children
        :param index: Index of node to heapify down
        :return:
        """
        if self.has_left_child(index):
            small_child_index = self.get_left_child_index(index)
            if self.has_right_child(index):
                right_child_index = self.get_right_child_index(index)
                if (self.items[right_child_index] < self.items[
                        small_child_index]):
                    small_child_index = right_child_index

            if self.items[index] > self.items[small_child_index]:
                self.swap(index, small_child_index)
                self.heapify_down(small_child_index)

    def __iter__(self):
        return iter(self.items)

    def preorder_traversal(self) -> Iterable:
        """
        Travers the parent, the left children, then the right children
        :return: Iterable of pre order Tree
        """
        return iter(self._preorder_traversal(0))

    def _preorder_traversal(self, index):
        if self.items[index] is not None:
            yield self.items[index]
            if self.has_left_child(index):
                yield from self._preorder_traversal(self.get_left_child_index(
                    index))
            if self.has_right_child(index):
                yield from self._preorder_traversal(self.get_right_child_index(
                    index))

    def inorder_traversal(self)-> Iterable:
        """
        Traverse the left children, the parent, then the right chilren
        :return: Iterable of in order Tree
        """
        return iter(self._inorder_traversal(0))

    def _inorder_traversal(self, index):
        if self.items[index] is not None:
            if self.has_left_child(index):
                yield from self._inorder_traversal(
                    self.get_left_child_index(index))
            yield self.items[index]
            if self.has_right_child(index):
                yield from self._inorder_traversal(
                    self.get_right_child_index(index))

    def postorder_traversal(self)-> Iterable:
        """
        Travers the left children, then the right children, then the parent
        :return: Iterable of post order Tree
        """
        return iter(self._postorder_traversal(0))

    def _postorder_traversal(self, index):
        if self.items[index] is not None:
            if self.has_left_child(index):
                yield from self._postorder_traversal(self.get_left_child_index(
                    index))
            if self.has_right_child(index):
                yield from self._postorder_traversal(
                    self.get_right_child_index(index))
            yield self.items[index]


class TestMinHeap(unittest.TestCase):

    def test_peek(self):
        test_min_heap = MinListHeap()
        for i in range(7):
            test_min_heap.add(i)
        self.assertEqual(test_min_heap.peek(), 0)

    def test_poll(self):
        test_min_heap = MinListHeap()
        for i in range(7):
            test_min_heap.add(i)
        test_min_heap.poll()
        self.assertListEqual(list(test_min_heap.preorder_traversal()),
                             [1, 3, 6, 4, 2, 5])
        test_min_heap.poll()
        self.assertListEqual(list(test_min_heap.preorder_traversal()),
                             [2, 3, 6, 4, 5])

    def test_add(self):
        test_min_heap = MinListHeap()
        for i in range(7):
            test_min_heap.add(i)
        self.assertListEqual(list(test_min_heap), list(range(7)))

    def test_traversal(self):
        test_min_heap = MinListHeap()
        for i in range(7):
            test_min_heap.add(i)
        self.assertListEqual(list(test_min_heap.preorder_traversal()),
                             [0, 1, 3, 4, 2, 5, 6])
        self.assertListEqual(list(test_min_heap._inorder_traversal(0)),
                             [3, 1, 4, 0, 5, 2, 6])
        self.assertListEqual(list(test_min_heap.postorder_traversal()),
                             [3, 4, 1, 5, 6, 2, 0])


if __name__ == '__main__':
    unittest.main()
