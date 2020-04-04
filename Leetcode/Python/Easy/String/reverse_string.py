def reverse_string(string):
    
    if len(string) <= 1:
        return string
    
    start = 0
    end = len(string)-1
    
    while start <= end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
        
    return string

input = ["h","e","l","l","o"]
input = ["H","a","n","n","a","h"]
print(reverse_string(input))