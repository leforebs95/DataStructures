from DataStructures.nodes import TreeNode


class MaxNodeHeap:
    def __init__(self):
        self.root = TreeNode()

    def __getitem__(self, item):
        self.__getitem(self.root, item)

    def __getitem(self, node, item):
        if node == item:
            return node
        if node.left:
            pass

    def __setitem__(self, key, value):
        pass
