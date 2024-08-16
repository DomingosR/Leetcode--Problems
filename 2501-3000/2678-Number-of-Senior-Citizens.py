class Solution(object):
    def countSeniors(self, details):
        return len([detail for detail in details if int(detail[11:13]) > 60])