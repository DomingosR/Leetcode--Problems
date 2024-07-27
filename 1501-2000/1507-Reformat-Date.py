class Solution(object):
    def reformatDate(self, date):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", \
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        spaces = [i for i in range(len(date)) if date[i] == " "]
        firstSpace = spaces[0]
        secondSpace = spaces[1]
        
        day = date[:firstSpace-2]
        dayStr = ("" if len(day) == 2 else "0") + day
        month = date[firstSpace+1:secondSpace]
        monthIndex = months.index(month) + 1
        monthStr = ("" if monthIndex >= 10 else "0") + str(monthIndex)
        year = date[secondSpace+1:]
        
        return "".join([year, "-", monthStr, "-", dayStr])