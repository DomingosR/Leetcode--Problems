class LockingTree(object):

    def __init__(self, parent):
        self.parent = parent
        self.locked = defaultdict(int)
        self.children = defaultdict(set)
        for i, parentI in enumerate(parent):
            if parentI != -1:
                self.children[parentI].add(i)

    def lock(self, num, user):
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False
        
    def unlock(self, num, user):
        if num not in self.locked or self.locked[num] != user:
            return False
        self.locked.pop(num)
        return True

    def upgrade(self, num, user):
        # Check if node or any ancestor is locked
        currentNum = num
        while currentNum > -1:
            if currentNum in self.locked:
                return False
            currentNum = self.parent[currentNum]
        
        # Check if any descendant is locked, unlock it
        foundLocked = False
        nodeQueue = deque()
        nodeQueue.appendleft(num)
        
        while nodeQueue:
            currentNum = nodeQueue.pop()
            for child in self.children[currentNum]:
                if child in self.locked:
                    foundLocked = True
                    self.locked.pop(child)
                nodeQueue.appendleft(child)
        
        # If a locked descendant is found, upgrade node
        if foundLocked:
            self.locked[num] = user
            return True
        
        return False