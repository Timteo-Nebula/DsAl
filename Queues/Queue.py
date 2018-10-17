class Queue(object):
    def __init__(self):
        """
        Implement a queue with python native data structure
        List, assuming the list head is the queue rear.
        head--------------list----------------tail
        rear--------------queue--------------front
        FIFO, items enter from the rear end, leave from the front end
        """
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """
        O(n). Since we insert one item to the specified position,
            we need move all elements with bigger indices backwards to
            the tail, leading a scan of these elements.
        NOTICE: Not all enqueue operation have O(n) time complexity.
                It's O(n) here for we use List.insert() to do enqueue.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        O(1) because List.pop() has O(1) time complexity.
        NOTICE: List.pop(n) has O(n) time complexity.
        """
        return self.items.pop()

    def size(self):
        return len(self.items)
