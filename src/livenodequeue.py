# File: livenodequeue.py
# Description: LiveNodeQueue class, containing priority queue, 
#              used to store live nodes in order
# Credits: Damianus Clairvoyance DP (13520035)

class LiveNodeQueue:
    # default constructor
    def __init__(self):
        self.queue = []
    
    # check if priority queue is empty
    def isEmpty(self):
        return (len(self.queue) == 0)
    
    # insert node in increasing cost order
    def enqueue(self, node):
        index = 0
        if (not self.isEmpty()):
            while (index < len(self.queue) and self.queue[index].cost < node.cost):
                index += 1
        self.queue.insert(index, node)
    
    # delete node with least cost (at first position)
    def dequeue(self):
        if (not self.isEmpty()):
            node = self.queue[0]
            self.queue.pop(0)
            return node
        return None