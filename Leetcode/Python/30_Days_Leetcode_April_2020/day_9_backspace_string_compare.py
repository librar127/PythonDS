def backspaceCompare_ON(S, T):
    #O(N)  Space and Time Solution
    S_ON_Space = []
    T_ON_Space = []
    
    for each in S:
        if each == '#':
            if len(S_ON_Space) > 0:
                S_ON_Space.pop()
        else:
            S_ON_Space.append(each)
    
    for each in T:
        if each == '#':
            if len(T_ON_Space) > 0:
                T_ON_Space.pop()
        else:
            T_ON_Space.append(each)
                
    if S_ON_Space == T_ON_Space:
        return True
    else:
        return False
    
import itertools
def yieldFunction(items):
    count = 0
    for each in items[::-1]: # or reversed(items)
        if each == '#':
            count += 1
        elif count > 0:
            count -= 1
        else:
            yield each
            
    return each 
    
    
def backspaceCompare_O1(S, T):    
    #O(1)  Space and O(N) Time Solution 
   return all(a==b for (a, b) in itertools.zip_longest(yieldFunction(S), yieldFunction(T)))


def backspaceCompare_2Pointers(S, T):
    #O(N)  Space and O(1) Time Solution - Assuming input is list which we can modify
    S = '# A C # # 9'.split()
    T = '# A C # B 9'.split()
    
    def modify_list(S):
        for index, each in enumerate(S):
            if each == '#':
                if index -1 >= 0:
                    S[index-1] = '#'
        
        S = [each for each in S if each != '#']
        
        return S
    
    return modify_list(S) ==  modify_list(T)
            
            

S = "#AC##9"
T = "#AC#B9"
print(backspaceCompare_2Pointers(S, T))