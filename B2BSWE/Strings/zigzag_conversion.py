
class Solution:
    def zigzag(self, s, rows):
        '''
        :type s: str
        :type rows: int
        :rtype: str
        '''
        if rows <=1:
            return s
        
        result = {each:[] for each in range(rows)}  
        
        diff = 1
        diff_sign = 1
        rows_copy = -1
        
        for _, each in enumerate(s):
            if rows_copy == rows-1:
                diff_sign = -1
            elif rows_copy == 0:
                diff_sign = 1
            
            rows_copy = rows_copy + diff * diff_sign  
            result[rows_copy].append(each)
            
            #print(rows_copy, each, result)
        res_string = ""
        for each in result:
            res_string += ''.join(result[each])
            
        return res_string

s = Solution() 
string = "YELLOWPINK" 
rows = 4
print(s.zigzag(string, rows))