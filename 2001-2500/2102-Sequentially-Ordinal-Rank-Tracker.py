from sortedcontainers import SortedList

class SORTracker:
    def __init__(self):
        self.locationList = SortedList()
        self.numQueries = 0
        
    def add(self, name, score):
        self.locationList.add((-score, name))
        
    def get(self):
        self.numQueries += 1
        return self.locationList[self.numQueries - 1][1]