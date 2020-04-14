def hamming_weight(n):
    count = 0
    while n:
        count += 1
        n = n & (n-1)
        
    return count

def hammingDistance(x, y):
    count = hamming_weight(x^y)
    return count

x = 1
y = 4
print(hammingDistance(x, y))