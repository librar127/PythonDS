class Solution:
    def isHappy(self, n):
        seen_set = set()
        while n > 1:
            sum = 0
            while n>0:
                sum += (n%10)**2
                n = n//10
            
            if sum in seen_set:
                return False
            else:
                seen_set.add(sum)
                
            n = sum
            
        return True
            
s = Solution()
print(s.isHappy(20))      