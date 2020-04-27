class Solution:
    def subarraySum_bf(self, nums, k):
        
        sum_cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                sum = 0
                for k in range(i, j):
                    sum += nums[k]
                    
                if sum ==s:
                    sum_cnt += 1
                
        return sum_cnt
    
    def subarraySum_hint2(self, nums, k):
        sum_count = 0
        sum = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            sum[i] = sum[i-1] + nums[i-1]
        print(sum)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if (sum[j] - sum[i]) == k:
                    sum_count += 1
                    
                    
        return sum_count
    
    def subarraySum(self, nums, k):
        count = s = 0
        Map = {}
        Map[0] = 1 
        for i in range(len(nums)):
            s += nums[i]
            if s - k in Map:
                count += Map.get(s-k)
            Map[s] = Map.get(s,0) +1 
        return count 
        
        
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