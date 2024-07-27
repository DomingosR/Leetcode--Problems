class Solution(object):
    def findHighAccessEmployees(self, access_times):
        def timeDiff(time1, time2):
            hour1, hour2 = int(time1[:2]), int(time2[:2])
            min1, min2 = int(time1[2:]), int(time2[2:])
            
            return 60 * (hour2 - hour1) + (min2 - min1)
        
        accessTimes = defaultdict(list)
        for employee, time in access_times:
            accessTimes[employee].append(time)
            
        highAccessEmployees = []
        
        for employee in accessTimes:
            timesList = sorted(accessTimes[employee])
            for i in range(len(timesList) - 2):
                time1, time2 = timesList[i], timesList[i+2]
                if timeDiff(time1, time2) < 60:
                    highAccessEmployees.append(employee)
                    break
                    
        return highAccessEmployees