import random
import unittest
from functools import total_ordering
from DataStructures.linkedlist import DoubleLinkedList


@total_ordering
class TreeNode:
    def __init__(self, value: object=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if self.value == other:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value < other:
            return True
        else:
            return False


class MinHeap:
    def __init__(self):
        self.items = DoubleLinkedList()

    def __repr__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    # def __getitem__(self, item):

    @staticmethod
    def get_left_child_index(parent_index):
        return 2 * parent_index + 1

    def get_left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    @staticmethod
    def get_right_child_index(parent_index):
        return 2*parent_index+2

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
        (self.items[index_one], self.items[index_two]) = \
         (self.items[index_two], self.items[index_one])

    def peek(self):
        return self.items[0]

    def poll(self):
        item = self.items[0]
        self.items[0] = self.items[len(self) - 1]
        del self.items[len(self)-1]
        print(self.items)
        self.heapify_down(0)
        return item

    def add(self, item):
        self.items.append(item)
        self.heapify_up(len(self)-1)

    def heapify_up(self, index):
        if self.has_parent(index):
            parent = self.get_parent(index)
            if parent > self.items[index]:
                parent_index = self.get_parent_index(index)
                self.swap(parent_index, index)
                self.heapify_up(parent_index)

    def heapify_down(self, index):
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

    def preorder_traversal(self):
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

    def inorder_traversal(self):
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

    def postorder_traversal(self):
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
        test_min_heap = MinHeap()
        for i in range(7):
            test_min_heap.add(i)
        self.assertEqual(test_min_heap.peek(), 0)

    def test_poll(self):
        test_min_heap = MinHeap()
        for i in range(7):
            test_min_heap.add(i)
        test_min_heap.poll()
        print(list(test_min_heap.preorder_traversal()))

    def test_add(self):
        test_min_heap = MinHeap()
        for i in range(7):
            test_min_heap.add(i)
        self.assertListEqual(list(test_min_heap), list(range(7)))

    def test_traversal(self):
        test_min_heap = MinHeap()
        for i in range(7):
            test_min_heap.add(i)
        self.assertListEqual(list(test_min_heap.preorder_traversal()),
                             [0, 1, 3, 4, 2, 5, 6])
        self.assertListEqual(list(test_min_heap._inorder_traversal(0)),
                             [3, 1, 4, 0, 5, 2, 6])
        self.assertListEqual(list(test_min_heap.postorder_traversal()),
                             [3, 4, 1, 5, 6, 2, 0])


class BinaryTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, value):
        if self.root.value is None:
            self.root = TreeNode(value)
        else:
            self.__setitem__(self.root, value)

    def find(self, value):
        return self.__getitem__(value)

    def __repr__(self):
        return str(list(self))

    def __getitem__(self, value):
        current_node = self.root
        while current_node:
            if current_node == value:
                break
            elif value < current_node:
                current_node = current_node.left
            elif value > current_node:
                current_node = current_node.right
        return current_node

    def __setitem__(self, key, value):
        if value < key:
            if key.left is None:
                key.left = TreeNode(value)
            else:
                self.__setitem__(key.left, value)
        elif value > key:
            if key.right is None:
                key.right = TreeNode(value)
            else:
                self.__setitem__(key.right, value)

    def __iter__(self):
        return iter(self._recur_iter(self.root))

    def _recur_iter(self, node):
        if node is not None:
            if node.left is not None:
                yield from self._recur_iter(node.left)
            yield node
            if node.right is not None:
                yield from self._recur_iter(node.right)


class TestBinaryTree(unittest.TestCase):
    def test_insert(self):
        test_tree = BinaryTree()
        for i in random.sample(range(7), 7):
            test_tree.insert(i)
        self.assertListEqual(list(test_tree), list(range(7)))

    def test_find(self):
        test_tree = BinaryTree()
        for i in random.sample(range(1, 100000), 9999):
            test_tree.insert(i)
        seek = test_tree.find(666)
        print(seek)
        if seek:
            self.assertEqual(seek, 666)
        else:
            self.assertIsNone(seek)


if __name__ == '__main__':
    unittest.main()
