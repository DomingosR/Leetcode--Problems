class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dictionary = dict()
        self.first = Node(0, 0)
        self.last = Node(0, 0)
        self.first.next = self.last
        self.last.prev = self.first

    def get(self, key):
        if key in self.dictionary:
            n = self.dictionary[key]
            self.removeNode(n)
            self.addNode(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dictionary:
            self.removeNode(self.dictionary[key])
        n = Node(key, value)
        self.addNode(n)
        self.dictionary[key] = n
        if len(self.dictionary) > self.capacity:
            n = self.first.next
            self.removeNode(n)
            del self.dictionary[n.key]

    def removeNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def addNode(self, node):
        p = self.last.prev
        p.next = node
        self.last.prev = node
        node.prev = p
        node.next = self.last