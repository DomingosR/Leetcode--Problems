class Solution(object):
    def countAnagrams(self, s):
        p = 10 ** 9 + 7
        
        def nChooseK(n, k):
            if k > n // 2:
                k = n - k
            
            if k == 0:
                return 1
            
            if k == 1:
                return n
            
            numerator, denominator = 1, 1
            for i in range(n-k+1, n+1):
                numerator *= i
                denominator *= (n + 1 - i)
            
            return (numerator // denominator) % p
        
        def arrayPerms(n, inputList):
            # It is assumed that input list is sorted in descending order,
            # and its values sum to n
            if len(inputList) == 1:
                return 1
            return (nChooseK(n, inputList[0]) * arrayPerms(n - inputList[0], inputList[1:])) % p
            
        def countPerms(word):
            letterCounter = Counter(word).values()
            letterCounter.sort(reverse = True)
            return arrayPerms(len(word), letterCounter)
                      
        numAnagrams = 1
        for word in s.split(" "):
            numAnagrams = numAnagrams * countPerms(word) % p
            
        return numAnagrams