'''
# Can not modify string as they are immutable
def helper(start, end, s):
    if start > end:
        return 
    
    s[start], s[end] = s[end], s[start]
    helper(start+1, end-1, s)

def reverse(s):
    
    helper(0, len(s)-1, s)
    
    return
'''
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:])+s[0]
         
s = 'Kumar' 
print(reverse(s))