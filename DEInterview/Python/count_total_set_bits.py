def countSetBits(num):
    result = 0
    mask = 1
    for each in range(1, num+1):  
        while each > 0:
            if (each & mask) == 1:
                result += 1
            each = each >> 1
            
    return result


n = 17
print(countSetBits(n))