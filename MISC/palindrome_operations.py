class PalindromeOperations():
    def valid_palindrome_removal(self, string):
        start = 0
        end = len(string)-1
        flag = False
        valid_palindrome = True
        
        while start <= end:
            if string[start] == string[end]:
                start += 1
                end -= 1
            elif string[start+1] == string[end] and flag is False:
                start += 2
                end -= 1
                flag = True
            elif string[start] == string[end-1] and flag is False:
                start += 1
                end -= 2
                flag = True
            else:
                valid_palindrome = False
                break
            
        return valid_palindrome
    
    def valid_palindrome_removals(self, string, n):
        start = 0
        end = len(string)-1
        step_count = 0
        valid_palindrome = True
        
        while start <= end:
            if string[start] == string[end]:
                start += 1
                end -= 1
            elif string[start+1] == string[end] and step_count < n:
                start += 2
                end -= 1
                step_count += 1
            elif string[start] == string[end-1] and step_count < n:
                start += 1
                end -= 2
                step_count += 1
            else:
                if step_count < n:
                    start += 1
                    step_count += 1
                else:
                    valid_palindrome = False
        
        if step_count != n:
            valid_palindrome = False
                
        return valid_palindrome
        
s = PalindromeOperations()

string = 'raacecar' # true
print(s.valid_palindrome_removal(string))

string = 'rawer' #false
print(s.valid_palindrome_removal(string))

string, n = 'rawer', 2 #true
print(s.valid_palindrome_removals(string, n))

string, n = 'raaacecar', 2 #false 
print(s.valid_palindrome_removals(string, n))