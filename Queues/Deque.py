"""
 For Queue, we add items at the rear end and remove it at
 the front end. But for Deque(double end queue), new items
 can be added at either the front or the rear.
 Likewise, existing items can be removed from either end

 This property means Deque can act like either Queue or Stack
"""


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        """
        O(1)
        """
        self.items.append(item)

    def add_rear(self, item):
        """
        O(n)
        """
        self.items.insert(0, item)

    def remove_front(self):
        """
        O(1)
        """
        return self.items.pop()

    def remove_rear(self):
        """
        O(n)
        """
        return self.items.pop(0)

    def size(self):
        return len(self.items)
