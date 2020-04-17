# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = int(n-1) / 2
        start = 0
        end = n-1
        
        while start <= end:
            mid = int((n-1) / 2)
            
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    end = mid-1
                else:
                    return mid
            else:
                start = mid + 1
                
            