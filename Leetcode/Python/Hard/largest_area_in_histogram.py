class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self, item): 
        self.top += 1       
        self.stack.insert(self.top, item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            ret_val = self.stack[self.top]
            self.top -= 1 
            return ret_val 
        
    def is_empty(self):
        return self.top == -1
        
    def print_stack(self):
        #print(self.stack, self.top)
        if self.is_empty():
            print("Stack is empty")
            return 
        else:
            top_var = self.top
            while top_var >= 0:
                print(self.stack[top_var], )
                top_var -= 1
                
    def peek(self):
        return self.stack[self.top]
    
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) <= 0:
            return 0
        p_stack = Stack()
        h_stack = Stack()
        area = -99
        max_area = -99
        
        p_stack.push(0)
        h_stack.push(heights[0])
        i = 1
        while i < len(heights):
            #h_stack.print_stack()
            #p_stack.print_stack()
            if h_stack.peek() < heights[i]:
                h_stack.push(heights[i])
                p_stack.push(i)
            else:
                current_height = h_stack.peek()
                current_position = p_stack.peek()
                
                while not h_stack.is_empty() and current_height > heights[i]:  
                    
                    if h_stack.peek() < heights[i]:
                        break
                                      
                    current_height = h_stack.pop()
                    current_position = p_stack.pop() 
                                       
                    area = current_height * (i - current_position)
                    if area > max_area:
                        max_area = area
                
                if current_position < i: 
                    p_stack.push(current_position)
                else:
                    p_stack.push(i)      
                                                         
                h_stack.push(heights[i]) 
            
            i += 1
        
        while not h_stack.is_empty(): 
            #p_stack.print_stack()
            area = h_stack.pop() * (i - p_stack.pop())
            if area > max_area:
                max_area = area           
             
        return max_area