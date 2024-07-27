class Solution(object):
    def buyChoco(self, prices, money):
        lowPrice1, lowPrice2 = 101, 101

        for price in prices:
            if price <= lowPrice1:
                lowPrice1, lowPrice2 = price, lowPrice1
            elif price < lowPrice2:
                lowPrice2 = price

        if lowPrice1 + lowPrice2 <= money:
            return money - lowPrice1 - lowPrice2
        else:
            return money
