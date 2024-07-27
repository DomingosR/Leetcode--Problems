class Solution(object):
    def asteroidCollision(self, asteroids):
        remaining = []
        
        for asteroid in asteroids:
            while len(remaining) and asteroid < 0 and remaining[-1] > 0:
                if remaining[-1] == -asteroid: 
                    remaining.pop()
                    break
                elif remaining[-1] < -asteroid:
                    remaining.pop()
                    continue
                elif remaining[-1] > -asteroid:
                    break
            else:
                remaining.append(asteroid)
        return remaining        