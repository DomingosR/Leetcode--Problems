class Solution(object):
    def findRotateSteps(self, ring, key):
        ringLen = len(ring)
        keyLen = len(key)
        
        def distance(i, j):
            return min( (i-j) % ringLen, (j-i) % ringLen)
        
        ringPos = defaultdict(set)
        for i in range(ringLen):
            ringPos[ring[i]].add(i)
        
        minSteps = [[(ringLen + 1)] * ringLen for _ in range(keyLen)]
        
        for i in range(ringLen):
            currentChar = key[keyLen - 1]
            minSteps[keyLen - 1][i] = 1 + min(distance(i, j) for j in ringPos[currentChar])
            
        for step in range(keyLen - 2, -1, -1):
            currentChar = key[step]
            for i in range(ringLen):
                minSteps[step][i] = 1 + min(distance(i, j) + minSteps[step+1][j] for j in ringPos[currentChar])
                
        return minSteps[0][0]