class Solution:
    def sortedSquares(self, A): 
        
        min_index_A = A.index(min(A, key=abs))
        left_A = A[:min_index_A][::-1]
        right_A = A[min_index_A:]
        
        out_list = []
        len_left_A = len(left_A)        
        len_right_A = len(right_A)
        
        i = j = 0
        while i < len_left_A and j < len_right_A:
            if left_A[i]**2 < right_A[j]**2:
                out_list.append(left_A[i]**2)
                i += 1
            else:                
                out_list.append(right_A[j]**2)
                j += 1        
        
        #print(i, j, left_A, right_A)
        while i < len_left_A:
            out_list.append(left_A[i]**2)
            i += 1
                
        while j < len_right_A:
            out_list.append(right_A[j]**2)
            j += 1
            
        return out_list
        
s = Solution()
nums = [-4,-1,0,3,10]
print(s.sortedSquares(nums))