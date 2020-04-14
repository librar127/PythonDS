
# Approach 1
def hammingWeight(n):
    count = 0
    
    while n:
        count += n & 1
        n >>= 1
    return count

def hammingWeight_2(n):
    count = 0
    while n:
        n=n & (n-1)
        count += 1
        
    return count

n = 11
print(hammingWeight(n))
print(hammingWeight_2(n))