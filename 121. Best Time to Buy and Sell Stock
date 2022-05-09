class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
Runtime: 1172 ms, faster than 70.25% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 87.11% of Python3 online submissions for Best Time to Buy and Sell Stock.
        """
        buy = 0
        sell = 1
        
        max_profit = 0
        while sell < len(prices): 
            if prices[sell] - prices[buy]<=0: # find a lower buying price
                buy=sell
                sell+=1
            else: # try out different sell prices
                max_profit = max(max_profit, prices[sell] - prices[buy])
                sell+=1
        return max_profit
