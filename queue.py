# Completed implementationo of a queue ADT
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item) # put to beginning of list

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        """ Show contents of a queue
        """
        return self.items

"""
q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
print(q.show())
"""
