class Solution(object):
    def countDays(self, days, meetings):
        meetingDays = []
        
        for start, end in meetings:
            left = bisect_left(meetingDays, start)
            right = bisect_right(meetingDays, end)
            include = []
            if left % 2 == 0:
                include.append(start)
            if right % 2 == 0:
                include.append(end)
            meetingDays[left:right] = include
        
        k = len(meetingDays) // 2
        
        return days - (sum(meetingDays[1::2]) - sum(meetingDays[::2]) + k)