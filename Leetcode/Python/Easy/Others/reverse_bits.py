
def reverseBits(n):
    
    result = 0
    position = 31
    while n:
        result += (n & 1)<<position
        n = n >> 1
        position -= 1
            
    return result

print(reverseBits(4294967293))