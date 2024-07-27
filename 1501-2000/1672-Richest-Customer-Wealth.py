class Solution(object):
    def maximumWealth(self, accounts):
        return max([sum(accounts[i]) for i in range(len(accounts))])