

class Array:
    def __init__(self):
        """
        Hash array implementation, collisions will be managed with linked
        list or heap
        """
        self.size = 0

    def __len__(self):
        return self.size

    def add(self):
        self.size += 1
