class Solution:
    def intersection(self, nums1, nums2):
        hashset = set()
        
        for each in nums1:
            if each in nums2:
                hashset.add(each)
                
        return hashset