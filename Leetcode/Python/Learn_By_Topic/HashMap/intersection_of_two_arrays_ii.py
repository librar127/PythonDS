class Solution:
    def intersect(self, nums1, nums2):
        
        # current submitted solution        
        result = []
        hashmap = {}
        for each_1 in nums1:
            if each_1 in hashmap:
                hashmap[each_1] += 1
            else:
                hashmap[each_1] = 1
                
        for each in nums2:
            if each in hashmap and hashmap[each] > 0:
                result.append(each)
                hashmap[each] -= 1
        return result
    
s = Solution()
nums1, nums2 = [4,9,5], [9,4,9,8,4]
print(s.intersect(nums1, nums2)) 