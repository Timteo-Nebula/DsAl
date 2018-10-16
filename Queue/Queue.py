class Queue(object):
    def __init__(self):
        """
        Implement a queue with python native data structure
        List, assuming the list head is the queue rear
        """
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
