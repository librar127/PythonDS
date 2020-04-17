class Solution:
    def checkValidString(self, s):
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
string = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
print(s.checkValidString(string))