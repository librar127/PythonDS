class Solution:
    def subarraySum_bf(self, nums, k):
        sum_count = 0
        
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    sum_count += 1
                    
        return sum_count
    
    def subarraySum(self, nums, k):
        sum_count = 0
        hashmap = {}
        hashmap[0] = 1
        sum = 0
        
        for _, each in enumerate(nums):
            sum += each
            
            if sum-k in hashmap:
                sum_count += hashmap[sum-k]
                                
            hashmap[sum] = hashmap.get(sum, 0) + 1
                    
        return sum_count
    
        
        
s = Solution()
nums, k = [1,1,1], 2
print(s.subarraySum(nums, k))

nums = [28,54,7,-70,22,65,-6]
k = 100
print(s.subarraySum(nums, k))

nums = [0,0,0,0,0,0,0,0,0,0]
k=0
print(s.subarraySum(nums, k))

nums = [1,2,3]
k=3
print(s.subarraySum(nums, k))