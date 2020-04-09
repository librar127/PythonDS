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
            
    def reverseList(self, head):
        current = head
        prev = None
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev
            
    def isPalindrome(self):
        
        if self.head is None:
            return True
        
        slow = fast = head = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        
        self.printList(head)
        second = self.reverseList(slow)
        self.printList(head)
        if not fast:
            prev.next = None
        
        while second and head:
            if second.val == head.val:
                second = second.next
                head = head.next
            else:
                return False
        
        if second:
            return False
        if head:
            return False
        
        return True
        
            
l1 = LinkedList()
l1.addNode(1)
l1.addNode(2)
l1.addNode(2)
l1.addNode(1)
print(l1.isPalindrome())