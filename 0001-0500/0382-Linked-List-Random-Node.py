class Solution(object):

    def __init__(self, head):
        self.list = []
        current = head
        count = 0

        while current:
            self.list.append(current.val)
            count += 1
            current = current.next

        self.numNodes = count

    def getRandom(self):
        return self.list[random.randint(0, self.numNodes - 1)]
