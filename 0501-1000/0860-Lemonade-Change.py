class Solution(object):
    def lemonadeChange(self, bills):
        currentBills = [0, 0, 0]
        
        for bill in bills:
            if bill == 5:
                currentBills[0] += 1
                
            elif bill == 10:
                currentBills[1] += 1
                if currentBills[0] == 0:
                    return False
                else:
                    currentBills[0] -= 1
                 
            else:
                currentBills[2] += 1
                if currentBills[1] > 0 and currentBills[0] > 0:
                    currentBills[0] -= 1
                    currentBills[1] -= 1
                elif currentBills[0] >= 3:
                    currentBills[0] -= 3
                else:
                    return False
                
        return True