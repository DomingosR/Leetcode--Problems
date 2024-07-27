class Solution(object):
    def nthUglyNumber(self, n):
        if n == 1:
            return 1

        uglyNumbers = [1]
        pointers = [0, 0, 0]
        factors = [2, 3, 5]

        for i in range(1, n):
            candidates = [uglyNumbers[pointers[i]] * factors[i] for i in range(3)]  
            nextNum = min(candidates)
            uglyNumbers.append(nextNum)
            for j in range(3):
                if uglyNumbers[pointers[j]] * factors[j] == nextNum:
                    pointers[j] += 1

        return uglyNumbers[-1]