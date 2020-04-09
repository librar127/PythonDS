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
        output = []
        head = self.head
        while head:
            output.append(head.val)
            head = head.next
        print(output)
            
    def reverseList(self, head):
        current = head
        prev = None
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev
            
    def mergeTwoLists(self, l1, l2):
        
        head = self.head
        while l1 and l2:
            if l1.val <= l2.val:
                node = Node(l1.val)
                node.next = head
                head = node
                l1 = l1.next
            else:
                node = Node(l2.val)
                node.next = head
                head = node
                l2 = l2.next
        
        while l1:            
            node = Node(l1.val)
            node.next = head
            head = node 
            l1 = l1.next
            
        while l2:            
            node = Node(l2.val)
            node.next = head
            head = node
            l2 = l2.next
        
        head = self.reverseList(head) 
        self.head = head
            
l1 = LinkedList()
l1.addNode(4)
l1.addNode(2)
l1.addNode(1)
#l1.printList() 

l2 = LinkedList()
l2.addNode(5)
l2.addNode(3)
l2.addNode(1)
#l2.printList() 

l3 = LinkedList()
l3.mergeTwoLists(l1.head, l2.head)
l3.printList() 
