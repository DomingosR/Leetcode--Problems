class Solution(object):
    def soupServings(self, n):
        if n >= 5000:
            return 1
        
        preComputed = {}

        def probability(n1, n2):
            if (n1, n2) in preComputed:
                return preComputed[(n1, n2)]

            if n1 <= 0 and n2 <= 0:
                return 0.5

            if n1 <= 0:
                return 1
            
            if n2 <= 0:
                return 0
            
            values = [0] * 4
            for i in range(4):
                values[i] = probability(n1 - 4 + i, n2 - i)
                                        
            preComputed[(n1, n2)] = 0.25 * sum(values)
            return preComputed[(n1, n2)]

        n = (n + 24) // 25
        return probability(n, n)