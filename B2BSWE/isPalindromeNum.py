
class Solution:
    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
        
        new_x = 0
        old_x = x
        if x < 0:
            return False
        elif x%10 == x:
            return True
        else:
            while x > 0:
                rem = x%10
                new_x = new_x*10+rem
                x=x//10
            
            if new_x == old_x:
                return True
            else:
                return False
            
s = Solution()
ans = s.isPalindrome(323)
print(ans)