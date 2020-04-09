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
            
    def middleNode(self):
        
        outlist = []
        head = nextp = self.head
        #nextp = head
        while nextp and nextp.next:
            head = head.next
            nextp = nextp.next.next
            
        while head:
            outlist.append(head.val)
            head = head.next
             
        return outlist
    
        
            
ll = LinkedList()
ll.addNode(4)
ll.addNode(5)
ll.addNode(1)
ll.addNode(9)
ll.addNode(7)
ll.addNode(10)
ll.printList()
print(ll.middleNode(), '\n')

ll = LinkedList()
ll.addNode(5)
ll.addNode(1)
ll.addNode(9)
ll.addNode(7)
ll.addNode(10)
ll.printList()
print(ll.middleNode(), '\n')

ll = LinkedList()
ll.addNode(7)
ll.addNode(10)
ll.printList()
print(ll.middleNode())