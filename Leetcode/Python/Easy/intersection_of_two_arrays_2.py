class Solution:
    def intersect(self, nums1, nums2):
        result = []
        hash_nums1 = {}
        for each_1 in nums1:
            if each_1 in hash_nums1:
                hash_nums1[each_1] += 1
            else:
                hash_nums1[each_1] = 1
            
            
        for each_2 in nums2:
            if each_2 in hash_nums1 and hash_nums1[each_2] > 0:
                result.append(each_2)
                hash_nums1[each_2] -= 1
                      
        return result
    
s = Solution()  
print(s.intersect([1,2,2,1], [2,2]), '\n')    
print(s.intersect([4,4,4], [9,4]), '\n') 