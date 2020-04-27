class Solution:
    def longestCommonSubsequence(self, text1, text2):
        
        arr = []
        m = len(text1)
        n = len(text2)
        for i in range(m+1):
            arr.append([0]*(n+1))
   
        for i in range(0, m):
            for j in range(0, n):
                
                if text1[i] == text2[j]:
                    arr[i+1][j+1] = arr[i][j] + 1
                else:
                    arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])
                    
        return arr[m][n]
                
        