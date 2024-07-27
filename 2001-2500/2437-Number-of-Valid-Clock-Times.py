class Solution(object):
    def countTime(self, time):
        hour = time[:2]
        minute = time[-2:]
        
        if hour == "??":
            hourCount = 24
        elif hour[0] == "?":
            hourCount = 3 if int(hour[1]) <= 3 else 2
        elif hour[1] == "?":
            hourCount = 10 if int(hour[0]) <= 1 else 4
        else:
            hourCount = 1
            
        if minute == "??":
            minuteCount = 60
        elif minute[0] == "?":
            minuteCount = 6
        elif minute[1] == "?":
            minuteCount = 10
        else:
            minuteCount = 1
            
        return hourCount * minuteCount