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
    
    def removeNthFromEnd(self, n):
        # two pointer's approach
        # one start's from 0
        # second start from 0+n
        # when second reaches at the end - Delete the current.next
        
        np = self.head
        head = self.head
        while n>0:
            np = np.next
            n -= 1
        
        if np:
            while np.next:
                np = np.next
                head = head.next

            head.next = head.next.next
            self.head = head
        else:
            head = head.next
            self.head = head
            
            
ll = LinkedList()
ll.addNode(5)
ll.addNode(4)
ll.addNode(3)
ll.addNode(2)
ll.addNode(1)
ll.printList()
print()
ll.removeNthFromEnd(4)
ll.printList()
print()

ll = LinkedList()
ll.addNode(2)
#ll.addNode(1)
ll.printList()
print()
ll.removeNthFromEnd(1)
ll.printList()