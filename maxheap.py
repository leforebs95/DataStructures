import random
import unittest
from collections import deque

from DataStructures.nodes import TreeNode


class MaxNodeHeap:
    def __init__(self):
        """
        Max Heap implemented with nodes/pointers
        """
        self.root = TreeNode()
        self.size = 0

    def add(self, value):
        new_node = TreeNode(value)
        if self.root.value is None:
            self.root = new_node
        else:
            bit = deque(format(self.size+1, 'b'))
            bit.popleft()
            node = self.get_last(self.root, bit)
            if node.left is None:
                node.left = new_node
                new_node.parent = node
                self.heapify_up(new_node)
            else:
                node.right = new_node
                new_node.parent = node
                self.heapify_up(new_node)
        self.size += 1

    def get_last(self, node, bit):
        if len(bit) == 0:
            return node
        digit = int(bit.popleft())
        if digit == 1 and node.right is not None:
            node = self.get_last(node.right, bit)
        elif digit == 0 and node.left is not None:
            node = self.get_last(node.left, bit)
        return node

    def __len__(self):
        return self.size

    def peek(self):
        return self.root

    def poll(self):
        max_val = self.root.value
        bit = deque(format(self.size, 'b'))
        bit.popleft()
        last_node = self.get_last(self.root, bit)
        if last_node.parent is None:
            return max_val
        parent = last_node.parent
        if parent.left is last_node:
            self.swap(self.root, last_node)
            parent.left = None
        elif parent.right is last_node:
            self.swap(self.root, last_node)
            parent.right = None
        self.heapify_down(self.root)
        self.size -= 1
        return max_val

    def swap(self, node1, node2):
        node1.value, node2.value = node2.value, node1.value

    def heapify_up(self, node):
        if node.parent is not None:
            if node.parent < node:
                self.swap(node.parent, node)
                self.heapify_up(node.parent)

    def heapify_down(self, node):
        if node.left:
            larger_val = node.left
            if node.right:
                if node.right > node.left:
                    larger_val = node.right

            if node < larger_val:
                self.swap(node, larger_val)
                self.heapify_down(node)

    def __iter__(self):
        return iter(self.preorder_traversal(self.root))

    def preorder_traversal(self, node):
        if node is not None:
            yield node
            if node.left is not None:
                yield from self.preorder_traversal(node.left)
            if node.right is not None:
                yield from self.preorder_traversal(node.right)


class TestMaxNodeHeap(unittest.TestCase):

    def test_peek(self):
        test_min_heap = MaxNodeHeap()
        for i in random.sample(range(7), 7):
            test_min_heap.add(i)
        self.assertEqual(test_min_heap.peek(), 6)

    def test_poll(self):
        test_min_heap = MaxNodeHeap()
        for i in random.sample(range(7), 7):
            test_min_heap.add(i)
        self.assertEqual(test_min_heap.poll(), 6)
        self.assertEqual(test_min_heap.poll(), 5)
        self.assertEqual(test_min_heap.poll(), 4)
        self.assertEqual(test_min_heap.poll(), 3)
        self.assertEqual(test_min_heap.poll(), 2)
        self.assertEqual(test_min_heap.poll(), 1)
        self.assertEqual(test_min_heap.poll(), 0)

    def test_add(self):
        test_min_heap = MaxNodeHeap()
        for i in range(7):
            test_min_heap.add(i)
        self.assertListEqual(list(test_min_heap), [6, 3, 0, 2, 5, 1, 4])


