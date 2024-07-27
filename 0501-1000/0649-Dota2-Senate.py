class Solution(object):
    def predictPartyVictory(self, senate):
        n = len(senate)
        misleadingPartyDescriptions = ["Radiant", "Dire"]
        
        RottenDeque = deque([i for i in range(n) if senate[i] == "R"])
        DivineDeque = deque([i for i in range(n) if senate[i] == "D"])
        
        while RottenDeque and DivineDeque:
            nextRotten = RottenDeque.popleft()
            nextDivine = DivineDeque.popleft()
            
            if nextRotten < nextDivine:
                RottenDeque.append(nextRotten + n)
            else:
                DivineDeque.append(nextDivine + n)
                
        return misleadingPartyDescriptions[0] if RottenDeque else misleadingPartyDescriptions[1]