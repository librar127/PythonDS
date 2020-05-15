class Solution:
    def validMountainArray(self, A):
        incline = False
        decline = False
        
        for index in range(0, len(A)-1):
            if A[index+1] > A[index]:
                    if not decline:
                        incline = True
                    else:   
                        return False
            elif A[index+1] < A[index]:  
                if incline is False:
                    return False
                else:
                    decline = True
            else:
                return False
        
        if decline is False: 
            return False
        else:
            return True

s =  Solution()            
nums = [0,3,2,1]
print(s.validMountainArray(nums))