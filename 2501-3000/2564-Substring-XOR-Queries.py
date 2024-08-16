class Solution(object):
    def substringXorQueries(self, s, queries):
        stringLocations = defaultdict(lambda: [-1, -1])
        i = s.find("0")
        if i >= 0:
            stringLocations[0] = [i, i]
        
        for i, char in enumerate(s):
            if char != "0":
                currentVal = 0
                for j in range(i, min(i + 30, len(s))):
                    currentVal = 2 * currentVal + int(s[j])
                    if currentVal not in stringLocations:
                        stringLocations[currentVal] = [i, j]
        
        return [stringLocations[first ^ second] for first, second in queries]