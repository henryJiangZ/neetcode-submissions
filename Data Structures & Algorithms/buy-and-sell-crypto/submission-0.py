class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < bought:
                bought = prices[i]
            elif(prices[i] - bought > profit):
                profit = prices[i] - bought
        return profit
