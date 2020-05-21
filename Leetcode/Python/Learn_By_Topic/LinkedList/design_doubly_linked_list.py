class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        
        count = 0
        head = self.head
        
        if head is None:
            return -1
        else:
            while count < index and head is not None:
                head = head.next
                count += 1
            if head is None:
                return -1
            else:
                return head.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        
        if self.head is None:
            self.head = node
        else:
            head = self.head
            head.prev = node
            node.next = head
            self.head = node
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        
        head = self.head
        if head is None:
            self.head = node
        else:
            while head.next is not None:
                head = head.next
            node.prev = head
            head.next = node            
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        head = self.head
        node = Node(val)        
        
        if index == 0:
            node.next = head
            self.head = node
            return
        
        count = 0
        prev = None
        while count < index:
            prev = head
            head = head.next
            count += 1
        
        node.next = prev.next
        node.prev = prev
        prev.next = node
        prev.next.prev = node
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return
            
        head = self.head
        current = head
        
        if index == 0:
            next = head.next
            if next:
                next.prev = None
            self.head = next
            return
            
        
        count = 0        
        while head and count < index:
            prev = head
            head = head.next
            count += 1
        
        if head is None:
            return
        else:
            #prev.next = head.next
            #del head
            prev.next = head.next
            if head.next:
                head.next.prev = prev
            head.prev = None
            head.next = None
            del head

        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)