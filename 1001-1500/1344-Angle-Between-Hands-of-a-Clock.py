class Solution(object):
    def angleClock(self, hour, minutes):
        angHour = ((hour % 12) + (minutes / 60.0)) * 30.0
        angMinute = 6.0 * minutes
        angDiff = abs(angHour - angMinute)
        
        return min(angDiff, 360 - angDiff)