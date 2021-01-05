
class Solution:
    def rotate(self, matrix):
        '''
        :type matrix: list of list of int
        :rtype: list of list of int
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        #result = [[0]*rows]*cols    
        result = [[None]*rows for _ in range(cols)]    
        
        for i in range(rows):
            for j in range(cols) :
              col = cols - i - 1
              result[j][col] = matrix[i][j]
        
        return result


s = Solution()
arr = [
  [ 1,  2,  3, 4],
  [ 5,  6,  7, 8],
  [ 9, 10, 11, 12],
  [13, 14, 15, 16]
]

result = s.rotate(arr)
print(result)