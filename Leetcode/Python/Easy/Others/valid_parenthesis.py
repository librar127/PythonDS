class Solution:
    def isValid(s):
        
        opening = ['[', '{', '(']
        closing = [']', '}', ')']
        bracket_list = []
        bracket_dict = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        
        for each in s:
            if each in opening:
                bracket_list.append(each)
            elif each in closing:
                if len(bracket_list) > 0 and bracket_list.pop() == bracket_dict[each]:
                    continue
                else:
                    return False
            else:
                return False
            
        
         
        if len(bracket_list) == 0:                
            return True
        else:
            return False
                    