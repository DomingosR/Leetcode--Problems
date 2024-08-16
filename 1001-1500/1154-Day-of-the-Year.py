class Solution(object):
    def dayOfYear(self, date):
        def isLeap(yearNo):
            return yearNo % 4 == 0 and yearNo != 1900
        
        numDaysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        yearNo = int(date[:4])
        monthNo = int(date[5:7])
        dayNo = int(date[-2:])
        
        return sum(numDaysPerMonth[:(monthNo - 1)]) + dayNo + (1 if isLeap(yearNo) and monthNo >= 3 else 0)
