def valid_palindrome(s):
    if len(s) <= 1:
        return True

    valid = True
    
    start = 0
    end = len(s)-1
    
    while start <= end:
        if s[start].isalnum():
            if s[end].isalnum():
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                    continue
                else:
                    valid = False
                break 
            else:
                end -= 1
                continue
        else:
            start += 1
    
    return valid

string = 'race a car'
string = "A man, a plan, a canal: Panama"
print(valid_palindrome(string))