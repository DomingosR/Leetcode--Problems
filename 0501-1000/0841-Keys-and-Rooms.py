class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        roomVisited = [1] + [0] * (n - 1)
        numVisited = 1
        roomQueue = deque()
        roomQueue.appendleft(0)

        while roomQueue:
            currentRoom = roomQueue.pop()
            nextRooms = rooms[currentRoom]
            for nextRoom in nextRooms:
                if roomVisited[nextRoom] == 0:
                    numVisited += 1
                    if numVisited == n:
                        return True
                    roomVisited[nextRoom] = 1
                    roomQueue.appendleft(nextRoom)
        
        return False