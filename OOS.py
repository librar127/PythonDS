
# coding: utf-8

# ### Logic gate implememtation using object oriented programming

# In[28]:


class LogicGate():
    
    def __init__(self, n):
        self.label = n
        
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


# In[32]:


class BinaryGate(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self, n)
        
        self.pinA = None
        self.pinB = None
        
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for Gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()
        
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for Gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()
        
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Can't Connect: NO EMPTY PINS")

class AndGate(BinaryGate):
    
    def __init__(self, n):
        super(AndGate, self).__init__(n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a==1 and b == 1:
            return 1
        else:
            return 0
        
        
class OrGate(BinaryGate):
    
    def __init__(self, n):
        super(OrGate, self).__init__(n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a==1 or b == 1:
            return 1
        else:
            return 0
    


# In[33]:


class UnaryGate(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self, n)
        
        self.pin = None
        
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin for Gate: "+ self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()
        
    def setNextPin(self, source):
        
        if self.pin == None:
            self.pin = source
        else:
            print("Can't connect: NO EMPTY PIN on this Gate")
            
class NotGate(UnaryGate):
    
    def __init__self():
        super(NotGate, self).__init__(n)
        
    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


# In[36]:


class Connector:
    
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.setNextPin(self)
        
    def getFrom(self):
        return self.fromgate
    
    def getTo():
        return self.togate
    


# In[37]:


def main():

    g1 = AndGate('G1')
    g2 = AndGate('G2')
    
    g3 = OrGate('G3')
    g4 = NotGate('G4')
    
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    
    c3 = Connector(g3, g4)
    
    print(g4.getOutput())
    
main()

