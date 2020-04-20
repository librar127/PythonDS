class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
        
s = Solution()
nums = [4,5,6,7,0,1,2]
print(s.search(nums, 7))

nums = [5,7,8,9,10,11,13,0,1]
print(s.search(nums, 0))

nums = [3,5,1,2]
print(s.search(nums, 0))

nums = [2,3,5,1]
print(s.search(nums, 0))

nums = [1]
print(s.search(nums, 0))
                
        
        # 2. Search for the given item