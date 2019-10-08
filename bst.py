import random
import unittest

from DataStructures.nodes import TreeNode


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
