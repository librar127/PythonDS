def isValidParenthesis(input):
    L_PAREN = ['(', '[', '{']    
    R_PAREN = [')', ']', '}']
    VALID_PAIR = {'(':')', '[':']', '{':'}'}
    
    stack = []
    for each in input:
        if each in L_PAREN:
            stack.append(each)
        elif each in R_PAREN:
            current = stack.pop()
            if each != VALID_PAIR[current]:
                return False
    
    return True

parenthesis_string = s = "()[]{"
parenthesis_string = "([)]"
parenthesis_string = "{[]}"
print(isValidParenthesis(parenthesis_string))