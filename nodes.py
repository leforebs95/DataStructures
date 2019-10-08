from functools import total_ordering


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
