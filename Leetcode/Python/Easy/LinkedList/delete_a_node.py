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
            print(head.val)
            head = head.next
            
    def deleteNode(self, x):
        head = self.head
        if x == head.val:
            if head.next:
                head.val = head.next.val
                head.next = head.next.next
            else:
                head = None    
            
        while head.next:
            if head.next.val == x:
                if head.next.next:
                    head.next.val = head.next.next.val
                    head.next.next = head.next.next.next
                else:
                    head.next = None
                break
            else:
                head = head.next
                
        
            
ll = LinkedList()
ll.addNode(4)
ll.addNode(5)
ll.addNode(1)
ll.addNode(9)
ll.printList()
print()
ll.deleteNode(5)
ll.printList()

print()
ll.deleteNode(4)
ll.printList()