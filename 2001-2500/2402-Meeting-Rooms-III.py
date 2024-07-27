class Solution(object):
    def mostBooked(self, n, meetings):
        availableRooms = list(range(n))
        roomsInUse = []
        numMeetings = [0] * n
        
        for [startTime, endTime] in sorted(meetings):
            while roomsInUse and roomsInUse[0][0] <= startTime:
                [endTimeAux, roomNumber] = heappop(roomsInUse)
                heappush(availableRooms, roomNumber)
            
            if availableRooms:
                roomNumber = heappop(availableRooms)
                heappush(roomsInUse, [endTime, roomNumber])
            else:
                [nextTime, roomNumber] = heappop(roomsInUse)
                heappush(roomsInUse, [nextTime + endTime - startTime, roomNumber])
            
            numMeetings[roomNumber] += 1
        
        return numMeetings.index(max(numMeetings))
