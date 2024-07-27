class Solution(object):
    def change(self, amount, coins):
        preComputed = {}
        coins.sort()

        def numCombinations(currentVal, lastCoin):
            if currentVal < coins[0]:
                return 1 if currentVal == 0 else 0

            if (currentVal, lastCoin) in preComputed:
                return preComputed[(currentVal, lastCoin)]

            returnVal = 0
            for coin in coins:
                if coin <= min(currentVal, lastCoin):
                    returnVal += numCombinations(currentVal - coin, coin)

            preComputed[(currentVal, lastCoin)] = returnVal
            return returnVal

        return numCombinations(amount, coins[-1])
