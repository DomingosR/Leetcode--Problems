class Solution(object):
    def numberOfBeams(self, bank):
        n = len(bank)
        devicesPerRow = [bank[i].count("1") for i in range(n)]
        auxList = [devicesPerRow[i] for i in range(n) if devicesPerRow[i] > 0]
        return sum([d1 * d2 for d1, d2 in list(zip(auxList, auxList[1:]))])