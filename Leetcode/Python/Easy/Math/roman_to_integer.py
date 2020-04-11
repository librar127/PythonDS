def romanToInt(s):
    
    num_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    num = num_dict[s[0]]
    index = 1
    while index < len(s):
        char = s[index-1]
        if char == 'I' and s[index] == 'V':
            num += 3
        elif char == 'I' and s[index] == 'X':
            num += 8
                
        elif char == 'X' and s[index] == 'L':
            num += 30
        elif char == 'X' and s[index] == 'C':
            num += 80
                
        elif char == 'C' and s[index] == 'D':
            num += 300
        elif char == 'C' and s[index] == 'M':
            num += 800
        
        else:                
            num += num_dict[s[index]]
            
        index += 1
    
    return num

print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('LVIII'))
print(romanToInt('IX'))
print(romanToInt('XCIV'))
print(romanToInt('MCMXCIV'))