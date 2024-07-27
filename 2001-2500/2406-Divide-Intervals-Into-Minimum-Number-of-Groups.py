class Solution(object):
    def minGroups(self, intervals):
        numRooms = 0
        roomHeap = []
        intervals.sort()
        
        for a, b in intervals:
            if roomHeap:
                busyTime = roomHeap[0][0]
                if busyTime < a:
                    _, roomNo = heapq.heappop(roomHeap)
                    heapq.heappush(roomHeap, (b, roomNo))
                else:
                    numRooms += 1
                    heapq.heappush(roomHeap, (b, numRooms))
            else:
                numRooms += 1
                heapq.heappush(roomHeap, (b, numRooms))
                
        return numRooms