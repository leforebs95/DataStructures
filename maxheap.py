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

    def swap(self, node1, node2):
        node1.value, node2.value = node2.value, node1.value

    def heapify_up(self, node):
        if node.parent is not None:
            if node.parent < node:
                self.swap(node.parent, node)
                self.heapify_up(node.parent)

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

    def test_add(self):
        tst = MaxNodeHeap()
        tst.add(10)
        tst.add(12)
        print(list(iter(tst)))


