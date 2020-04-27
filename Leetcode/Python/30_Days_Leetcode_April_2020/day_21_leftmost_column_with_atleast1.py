# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        [row, col] = binaryMatrix.dimensions()
        
        min_index = 100
        found = False
        i = 0
        j = col-1
        
        while i < row and j >= 0:
            if binaryMatrix.get(i, j) == 0:
                i += 1
            else:
                found = True
                if min_index > j:
                    min_index = j
                j -= 1
                    
            print(i, j)

        if found == True:
            return min_index
        
        return -1
    
    def leftMostColumnWithOne_hint1(self, binaryMatrix: 'BinaryMatrix') -> int:
        [row, col] = binaryMatrix.dimensions()
        
        min_index = 100
        found = False
        for i in range(row):
            start = 0 
            end = col-1
            
            while start <= end:
                mid = (start+end)//2
                if binaryMatrix.get(i, mid) == 1: 
                    if mid == 0:
                        return 0
                        
                    if binaryMatrix.get(i, mid-1) == 0:
                        found = True
                        if min_index > mid:
                            min_index = mid
                        break
                    else:
                        end = mid - 1
                else:
                    start = mid + 1

        if found == True:
            return min_index
        
        return -1
            