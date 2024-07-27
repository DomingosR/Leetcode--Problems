class Solution(object):
    def countBeautifulPairs(self, nums):
        def gcd(num1, num2):
            while num1 % num2 > 0:
                num1, num2 = num2, num1 % num2
            return num2
        
        coprimePairs = set()
        
        for i in range(1, 10):
            for j in range(1, 10):
                if gcd(i, j) == 1:
                    coprimePairs.add((i, j))
                    
        countPairs = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                firstDigit = int(str(nums[i])[0])
                lastDigit = nums[j] % 10
                if (firstDigit, lastDigit) in coprimePairs:
                    countPairs += 1
                    
        return countPairs