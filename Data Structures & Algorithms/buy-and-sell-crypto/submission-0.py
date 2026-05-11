class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_Profit = 0
        min_buy = prices[0]
        
        for i in prices:
            max_Profit = max(max_Profit, i - min_buy)
            min_buy = min(min_buy, i)
        return max_Profit