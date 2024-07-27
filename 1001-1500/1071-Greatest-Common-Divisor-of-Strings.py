class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcd(n1, n2):
            while n2:
                n1, n2 = n2, n1 % n2
            return n1

        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(len(str1), len(str2))]
