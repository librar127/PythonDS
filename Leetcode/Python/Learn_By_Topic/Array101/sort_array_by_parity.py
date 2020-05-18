class Solution:
    def sortArrayByParity(self, A):
        
        if len(A) < 2:
            return A
        
        even_pointer = 0
        index = 0
        while index < len(A):
            if A[index]%2 != 0:
                pass
            else:
                A[even_pointer], A[index] = A[index], A[even_pointer]
                even_pointer += 1
            index += 1
                
        return A
    
s =Solution()
nums = [3,1,2,4]
print(s.sortArrayByParity(nums))