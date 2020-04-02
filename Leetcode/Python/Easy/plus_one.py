class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Add 1 to the last digit
        if digits[n-1] < 9:
            digits[n-1] = digits[n-1]+1
        else:
            digits[n-1] = 0
            k = n-2
            while k >= 0:
                if digits[k] == 9:
                    digits[k] = 0
                else:
                    num = digits[k]
                    digits[k] = num+1
                    break
                k = k-1
            
            if digits[0] == 0:
                digits.insert(0, 1)  
        
        return digits
    
s = Solution()
print(s.plusOne([9, 9, 9]))  
print(s.plusOne([2,4,9,3,9]))     