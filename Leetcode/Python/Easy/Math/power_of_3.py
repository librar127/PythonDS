import math
import numpy as np
import re

# Using Loop
def isPowerOfThree_Loop(n):
    
    if n < 0:
        return False
    
    power = 0
    num = 3
    
    while num**power <= n:
        if num**power == n:
            return True
        power += 1
        
    return False    

# Using Math as- 3**Power = n => power*log3 = log n  => power = (logn / log 3). power has to be an int for 3 to divide n. and hence if power%1==0 then True else False.
def isPowerOfThree_Math(n):
    return ((math.log10(n)/math.log10(3)) % 1) == 0
    
def isPowerOfThree_BaseConversion(n):
    if re.search('^10*$', np.base_repr(n, 3)):
        return True
    else:
        return False


print(isPowerOfThree_Loop(9))  
print(isPowerOfThree_Math(4))  
print(isPowerOfThree_BaseConversion(1)) 