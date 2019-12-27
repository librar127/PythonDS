class Solution:
    
    def parenthesis_generator(self, num_opening_parenthesis, num_closing_parenthesis, current_parenthesis, parenthesis_list):
        if num_opening_parenthesis<=0 and num_closing_parenthesis <= 0:
            parenthesis_list.append(current_parenthesis)
            return parenthesis_list
        
        if num_opening_parenthesis > 0:
            self.parenthesis_generator(num_opening_parenthesis-1, num_closing_parenthesis, current_parenthesis+"(", parenthesis_list)            
           
        if num_opening_parenthesis < num_closing_parenthesis:
            self.parenthesis_generator(num_opening_parenthesis, num_closing_parenthesis-1, current_parenthesis+")", parenthesis_list)
        
        return parenthesis_list
    
    def generateParenthesis(self, n):
        if n <=0:
            return []
        parenthesis_list = list()
        
        self.parenthesis_generator(n, n, '', parenthesis_list)
        return parenthesis_list
    
solution = Solution()
input_num = 2
print(solution.generateParenthesis(input_num))