class Stack:
    """
    Implement Stack with Python native data structure List,
    assuming the tail is the stack top.
    LIFO
    """

    def __init__(self): self.items = []

    def is_empty(self):
        """
        O(1)
        """
        return len(self.items) == 0

    def push(self, item):
        """
        O(1)
        """
        self.items.append(item)

    def pop(self):
        """
        O(1), Note that time complexity of pop(n) is O(n)
        """
        return self.items.pop()

    def peek(self):
        """
        O(1)
        """
        return self.items[-1]

    def size(self):
        """
        O(1)
        """
        return len(self.items)
