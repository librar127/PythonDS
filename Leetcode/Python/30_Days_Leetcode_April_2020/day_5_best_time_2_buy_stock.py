# This is alternative method where take the difference of every pair in creasing order and then take the sum of difference to find the max_profit
def get_max_profit_alternative(nums):
    max_profit = 0
    
    index = 0
    while index < len(nums)-1:
        if nums[index+1] > nums[index]:
            max_profit += nums[index+1] - nums[index]
        index += 1
            
    return max_profit


def get_max_profit(nums):
    buy = 0
    sell = 0
    index = 0
    max_profit = 0
    
    while index < len(nums)-1:
        while index < len(nums)-1 and nums[index] > nums[index+1]:
            index += 1
        buy = nums[index]
    
        while index < len(nums)-1 and nums[index] < nums[index+1]:
            index += 1   
        sell = nums[index]
        
        max_profit += sell - buy
        
        
    return max_profit

input = [1,2,3,4,5]
print(get_max_profit(input))
print(get_max_profit_alternative(input))

input = [7,1,5,3,6,4]
print(get_max_profit(input))
print(get_max_profit_alternative(input))