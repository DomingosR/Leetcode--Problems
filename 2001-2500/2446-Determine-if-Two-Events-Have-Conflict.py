class Solution(object):
    def haveConflict(self, event1, event2):
        def eventTimes(event):
            startHour = int(event[0][:2])
            startMin = int(event[0][3:])
            endHour = int(event[1][:2])
            endMin = int(event[1][3:])

            return [startHour, startMin, endHour, endMin]

        startHour1, startMin1, endHour1, endMin1 = eventTimes(event1)
        startHour2, startMin2, endHour2, endMin2 = eventTimes(event2)

        if endHour2 < startHour1 or (endHour2 == startHour1 and endMin2 < startMin1):
            return False
        if endHour1 < startHour2 or (endHour1 == startHour2 and endMin1 < startMin2):
            return False
        return True
