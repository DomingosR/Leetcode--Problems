class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        
        return sum([abs(seats[i] - students[i]) for i in range(len(seats))])