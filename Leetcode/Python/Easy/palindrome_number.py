import math

class Solution:
    ### Without converting the number into string 
    def isPalindrome(self, x):
        is_neg = x<1
        if is_neg:
            return False
        
        while x > 0:
            ### Extract number of digits in the input
            num_digits = int(math.log10(x))+1
            
            ### Extract first and last digits
            last_digit = x % 10
            first_digit = x // (10**(num_digits-1))
            
            ### Check if first and last digits are matching            
            if first_digit != last_digit:
                return False
            
            ### remove the first digit
            x = x % (10**(num_digits-1))
            
            ### remove the last digit
            x = x // 10
            
        return True        
        
    ### By converting the number into string  
    def isPalindrome_string(self, x):
        return str(x)==str(x)[::-1]
        
        
solution = Solution()
num = 10
print(solution.isPalindrome_string(num))
print(solution.isPalindrome(num))        