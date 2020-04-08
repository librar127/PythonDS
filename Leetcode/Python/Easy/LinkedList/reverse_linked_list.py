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
            
    def printList(self):
        head = self.head
        while head:
            print(head.val, )
            head = head.next
            
    def reverseList(self):
        current = self.head
        prev = None
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        self.head = prev
    
ll = LinkedList()
ll.addNode(5)
ll.addNode(4)
ll.addNode(3)
ll.addNode(2)
ll.addNode(1)
ll.printList()
print()
ll.reverseList()
ll.printList()   