class Solution:
    def reverse(self, x):
<<<<<<< HEAD
       
        
        
=======
              
>>>>>>> e6b271f08413af7110d4672987a29b3d5bf13ad0
        ### Check for Boundry condition
        if x == 0:
            return 0
        
        ### Check for the Allowed Range
        if x < -1*2**31:
            return 0
        elif x > 2**31-1:
            return 0
        
        ### Prepare for Negative Numbers
        neg_num = x<0
        if neg_num:
            x = x*-1
        
        ### Coding the actual Logic   
        output = ""
        while x>0:
            output += str(x%10)
            x = x//10
            
        ### Remove Leading Zeros
        output = output.strip("0");

        ### Handle Negative Numbers
        if neg_num:
            output = '-'+output   
        
        ### Check for the Allowed Range
        if int(output) < -1*2**31:
            return 0
        elif int(output) > 2**31-1:
            return 0
        
        return output
<<<<<<< HEAD
solution = Solution()
print(solution.reverse(100))
        
=======
        
solution = Solution()
print(solution.reverse(100))
        
>>>>>>> e6b271f08413af7110d4672987a29b3d5bf13ad0
