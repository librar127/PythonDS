class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        buy_day = 0
        sell_day = 0
        index = 0
        while index < len(prices)-1:
            while index < len(prices)-1 and prices[index] >= prices[index+1]:
                index += 1
            buy_day = prices[index]
            
            while index < len(prices)-1 and prices[index] < prices[index+1]:
                index += 1
                
            sell_day = prices[index]
            
            max_profit += sell_day - buy_day
             
        return max_profit
    
s = Solution()
print(s.maxProfit([3,3]))