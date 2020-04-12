class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def addNode(self, x):
        node = Node(x)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
    def printList(self, head):
        output = []
        #head = self.head
        while head:
            output.append(head.val)
            head = head.next
        print(output)
        
    def hasCycle(self):
        
        slow = fast = self.head
        while slow and fast:
            slow = slow.next
            fast = fast.next   
            if slow == fast:
                return True
            
            if fast.next:
                fast = fast.next
            else:
                return False
            
            if slow == fast:
                return True
            
        return False
        
        
            
l1 = LinkedList()
l1.addNode(1)
l1.addNode(2)
l1.addNode(2)
l1.addNode(1)
print(l1.hasCycle())