def missingNumber(nums):
    
    n = len(nums)
    sum = 0
    for each in nums:
        sum += each
    
    return n*(n+1)//2 - sum