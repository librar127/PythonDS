
import math

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
                
    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
        
        if x < 0:
            return False
        elif x%10 == x:
            return True
        else:
            num_digits = math.floor(math.log10(x)) + 1 
            for each in range(num_digits//2):
                print(each, x, x // 10**(num_digits-(each*2+1)), x % 10)
                if x // 10**(num_digits-(each*2+1)) == x % 10:                    
                    x %= 10**(num_digits-(each*2+1))
                    x //= 10
                    print(x)
                else:
                    return False
                    
        return True
            
s = Solution()
ans = s.isPalindrome(32)
print(ans)