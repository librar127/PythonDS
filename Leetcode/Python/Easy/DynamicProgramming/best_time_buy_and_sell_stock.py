class Solution:
    def maxProfit_bf(self, prices):
        
        max_profit = 0
        for index, _ in enumerate(prices):
            for j in range(index+1, len(prices)):
                if prices[j] - prices[index] > max_profit:
                    max_profit = prices[j] - prices[index]
                    
        return max_profit
    
    def maxProfit(self, prices):
        
        min_price = 99999999999999#Interger.MAX_VALUE
        max_profit = 0
        
        for _, each in enumerate(prices):
            
            if each < min_price:
                min_price = each
                
            elif max_profit < each - min_price:
                max_profit = each - min_price
                
        return max_profit