class Solution:
    
    
    # This correct implementation
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        index_i = 0
        index_j = 0
        loop_i = 0
        while loop_i < m and index_j < n:
            if nums1[index_i] <= nums2[index_j]:  
                index_i += 1
            else:                
                nums1.insert(index_i, nums2[index_j])
                nums1.pop()
                index_i += 1
                index_j += 1
                loop_i -= 1
                    
            loop_i += 1
                      
        while index_j < n:      
            #nums1[index_i] = nums2[index_j]
            nums1.insert(index_i, nums2[index_j])
            nums1.pop()
            index_i += 1
            index_j += 1
            
        return nums1
        
    # This is not accepted solution to leetcode as I assumed that when with 0 is included which was wrong. Check the correct solution above this
    def merge_2(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        
        # find the optimal point
        optimal_point = len(nums1)-n
        index_i = 0
        index_j = 0
        while index_i < len(nums1) and index_j < n:
            if nums1[index_i] <= nums2[index_j]:
                if nums1[index_i] == 0 and index_i >= optimal_point:
                    nums1[index_i] = nums2[index_j]
                    index_j += 1                        
                index_i += 1
            else:                
                nums1.insert(index_i, nums2[index_j])
                nums1.pop()
                optimal_point += 1
                index_i += 1
                index_j += 1
                
        return nums1

# ===================       
nums1 = [1,2,3,0,0,0]
m=6
nums2 = [2,5,6]
n = 3

print()
s = Solution()
print(s.merge_2(nums1, m, nums2, n))

# --------------------------------
nums1 = [1,4,8,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(s.merge_2(nums1, m, nums2, n))

# ================================
print()
nums1 = [1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n = 3
print(s.merge(nums1, m, nums2, n))

# --------------------------------
nums1 = [1,4,8,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(s.merge(nums1, m, nums2, n))