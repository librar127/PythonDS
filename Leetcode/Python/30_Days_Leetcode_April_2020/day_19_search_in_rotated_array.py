class Solution:
    def search(self, nums, target):
        
        # Two Step approach
        # 1. Find Pivot Element
        start = 0
        end = len(nums)-1
        
        while start < end:
            mid = (start + end )//2
            
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
                
        pivot = start
    

        start = 0
        end = len(nums)-1
        if target < nums[0]:
            start = pivot
        else:
            end = pivot-1
            
        while start <= end:
            mid = (start + end ) //2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid-1
                
        return -1
        
s = Solution()
nums = [4,5,6,7,0,1,2]
print(s.search(nums, 7))

nums = [5,7,8,9,10,11,13,0,1]
print(s.search(nums, 0))
                
        
        # 2. Search for the given item