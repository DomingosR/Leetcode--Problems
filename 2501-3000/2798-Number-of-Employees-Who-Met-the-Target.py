class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return len([1 for i in range(len(hours)) if hours[i] >= target])