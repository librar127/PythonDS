class Solution:
    
    ### Stack Solution - Time: O(N) Space: O(2N)
    def checkValidString(self, s):
        if len(s) == 0:
            return True
        
        if s[0] == ')':
            return False

        left_stack = []
        star_stack = []
        
        for index, each in enumerate(s):
            if each == '(':
                left_stack.append(index)
            elif each == '*':
                star_stack.append(index)
            else:
                if len(left_stack) > 0:
                    left_stack.pop()
                elif len(star_stack) > 0:
                    star_stack.pop()
                else:
                    return False
        
        print(left_stack, star_stack)
        index = len(left_stack)-1       
        while index >= 0:
            if len(star_stack) <= 0:
                return False
            else:  
                star_index = star_stack.pop()
                print(index, left_stack[index], star_index)
                if star_index < left_stack[index]:
                    return False
                else:
                    index -= 1
        
        return True
        
        
    def checkValidString_1(self, s):
        low = high = 0
        for i, _ in enumerate(s):
            if s[i] =='(':
                low += 1
                high += 1
            elif s[i] == '*':
                low -= 1
                high += 1
            else:
                low -= 1
                high -= 1
                
                if high<0:
                    break
                
            if(low<0):
                low=0
                
        return low==0
    
    
s = Solution()
string = "(*))))"
sytring = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
print(s.checkValidString(string))