def countAndSay(n):
    
    if n <= 0:
        return 0
    
    result = "1"
    if n == 1:
        return result 
    
    result = "11"
    if n == 2:
        return result
    
    freq = 0
    start = 2
    while start < n:
        temp_result = ""
        freq = 1
        index = 0
        
        while index < len(result)-1:
            while index < len(result)-1 and result[index] == result[index+1]:
                freq += 1
                index += 1
                
            temp_result += str(freq)+result[index]
            index += 1
            freq = 1
        
        if index == len(result) -1:
            temp_result += str(freq)+result[index]
            
        result = temp_result
        start += 1
        
    return result

input = 1
print(countAndSay(input))

input = 2
print(countAndSay(input))

input = 3
print(countAndSay(input))

input = 4
print(countAndSay(input))

input = 5
print(countAndSay(input))

input = 6
print(countAndSay(input))

input = 7
print(countAndSay(input))

input = 8
print(countAndSay(input))