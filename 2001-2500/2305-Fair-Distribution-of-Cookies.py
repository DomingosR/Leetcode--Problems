class Solution:
    def distributeCookies(self, cookies, k):
        returnVal = [10**6]
        cookieCount = [0] * k

        def backtrack(cookieNumber, cookies, k):
            if cookieNumber == len(cookies):
                maxVal = max(cookieCount)
                returnVal[0] = min(returnVal[0], maxVal)
                return

            for i in range(k):
                cookieCount[i] += cookies[cookieNumber]
                backtrack(cookieNumber + 1, cookies, k)
                cookieCount[i] -= cookies[cookieNumber]
                if cookieCount[i] == 0:
                    break
        
        backtrack(0, cookies, k)
        return returnVal[0]