class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.top_i = -1
        self.min = None
        

    def push(self, x):
            
        if self.top_i == -1:
            self.min = x
        else:
            #print(self.min, x)
            if self.min > x:
                self.min = x
        
        self.top_i +=1
        self.stack.insert(self.top_i, x)  
                
        
    def pop(self):
        if self.isEmpty():
            print("Empty Stack")
            return
        
        item_popped = self.stack.pop(self.top_i)
        self.top_i -= 1
        
        if self.isEmpty():
            self.min = None
        else: 
            if item_popped == self.min:                
                top = self.top_i 
                stack_min = self.stack[top]
                for i in range(self.top_i+1):
                    if self.stack[i] < stack_min:
                        stack_min = self.stack[i]
                        
                self.min = stack_min
            
    def top(self):
        return self.stack[self.top_i]

    def getMin(self):
        if self.isEmpty():
            print('EMpty Stack')
        return self.min
    
    def isEmpty(self):
        return self.top_i == -1
    
    def printStack(self):
        print(self.stack)