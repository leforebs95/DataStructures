import unittest

from DataStructures.nodes import TreeNode


class MaxNodeHeap:
    def __init__(self):
        self.root = TreeNode()

    def add(self, value):
        if self.root.value is None:
            self.root = TreeNode(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if node.left is None:
            node.left = TreeNode(value)
            node.left.parent = node
            self.heapify_up(node.left)
        elif node.right is None:
            node.right = TreeNode(value)
            node.right.parent = node
            self.heapify_up(node.right)
        else:
            self._add(node.left, value)

    def peek(self):
        return self.root

    def poll(self):
        max_val = self.root.value
        last_node = self.get_last(self.root)
        self.root.value = last_node.value
        self.heapify_down(self.root)
        return max_val

    def get_last(self, node):
        if node.right is not None:
            self.get_last(node.right)
        elif node.left is not None:
            self.get_last(node.left)
        else:
            return node

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
                self.heapify_down(larger_val)

    def __iter__(self):
        return iter(self._inorder_traversal(self.root))

    def _inorder_traversal(self, node):
        if node is not None:
            if node.left:
                yield from self._inorder_traversal(node.left)
            yield node
            if node.right:
                yield from self._inorder_traversal(node.right)


class TestMaxNodeHeap(unittest.TestCase):

    def test_peek(self):
        test_min_heap = MaxNodeHeap()
        for i in range(7):
            test_min_heap.add(i)
        self.assertEqual(test_min_heap.peek(), 6)

    def test_poll(self):
        test_min_heap = MaxNodeHeap()
        for i in range(7):
            test_min_heap.add(i)
        test_min_heap.poll()
        self.assertListEqual(list(test_min_heap),
                             [1, 3, 6, 4, 2, 5])
        test_min_heap.poll()
        self.assertListEqual(list(test_min_heap),
                             [2, 3, 6, 4, 5])

    def test_add(self):
        test_min_heap = MaxNodeHeap()
        for i in range(7):
            test_min_heap.add(i)
        print(list(test_min_heap))
        self.assertListEqual(list(test_min_heap), list(range(7)))


