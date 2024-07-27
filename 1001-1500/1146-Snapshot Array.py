class SnapshotArray(object):
        
    def __init__(self, length):
        self.values = [[[-1, 0]] for _ in range(length)]
        self.snapId = 0

    def set(self, index, val):
        self.values[index].append([self.snapId, val])

    def snap(self):
        self.snapId += 1
        return self.snapId - 1

    def get(self, index, snapId):
        i = bisect_left(self.values[index], [snapId + 1]) - 1
        return self.values[index][i][1]
