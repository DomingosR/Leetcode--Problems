class Node:
    def __init__(self, url):
        self.val = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, url):
        self.root = Node(url)

    def visit(self, url):
        newNode = Node(url)
        newNode.prev = self.root
        self.root.next = newNode
        self.root = self.root.next

    def back(self, steps):
        while steps and self.root.prev:
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps):
        while steps and self.root.next:
            self.root = self.root.next
            steps -= 1
        return self.root.val
