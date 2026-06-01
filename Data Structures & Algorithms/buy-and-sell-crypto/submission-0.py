class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = float('inf')
        maxProfit = 0
        for price in prices:
            if price < lowestPrice:
               lowestPrice = price

            currentProfit = price - lowestPrice

            if currentProfit > maxProfit:
                maxProfit = currentProfit
        return maxProfit

        