class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            
            if mid!=start and mid!=end:
                # no rotation if end is larger than start, monotonous array
                if nums[end] > nums[start]:
                    return nums[start]
                # if there is rotation
                else:
                    if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                        return nums[mid]
                    # rotation is in the second half
                    elif nums[mid] >= nums[start]:
                        start = mid+1                      
                    # rotation is in the first half
                    else:
                        end = mid - 1
            # only two elements left
            elif mid == start:
                return min(nums[start], nums[end]) 
                
        return nums[0]
        
        
s = Solution()
nums = [4,5,6,7,0,1,2]
print(s.findMin(nums))


nums = [3,5,1,2]
print(s.findMin(nums))