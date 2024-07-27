class Solution(object):
    def coinChange(self, coins, amount):
        coins.sort()
        minNum = [0] + [amount + 1] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    minNum[i] = min(minNum[i], minNum[i-coin] + 1)
                else:
                    break

        return minNum[amount] if minNum[amount] <= amount else -1
