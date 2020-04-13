def missingNumber(self, nums: List[int]) -> int:
    
    n = len(nums)
    sum = 0
    for each in nums:
        sum += each
    
    return n*(n+1)//2 - sum