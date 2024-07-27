class Solution(object):
    def halvesAreAlike(self, s):
        vowels = set("aeiouAEIOU")
        n = len(s) // 2
        
        return sum([1 for i in range(n) if s[i] in vowels]) == \
            sum([1 for i in range(n) if s[i+n] in vowels])