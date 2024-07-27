class Solution(object):
    def circularGameLosers(self, n, k):
        receivedBall = [False] * n
        currentIndex, i = 0, 1
        
        while not receivedBall[currentIndex]:
            receivedBall[currentIndex] = True
            currentIndex = (currentIndex + i * k) % n
            i += 1
            
        return [i+1 for i in range(n) if not receivedBall[i]]