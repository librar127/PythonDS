
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# Day 1 solution
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        # Create the node anyways
        node = Node(insertVal, None)
        
        # If the list is empty
        if not head:            
            node.next = node
            return node
        
        if head.next == head:
            head.next = node
            node.next = head
            
            return head
        
        toInsert = False
        prev = head
        current = head.next 
        while prev.next != head:
            
            if insertVal > prev.val and insertVal <= current.val:
                node.next = prev.next
                prev.next = node
                toInsert = True
                break
            elif prev.val > current.val and insertVal <= current.val:                
                node.next = current
                prev.next = node
                toInsert = True
                break
            elif prev.val > current.val and insertVal >= prev.val:                
                node.next = current
                prev.next = node
                toInsert = True
                break
                
            prev = prev.next
            current = current.next
            
        if not toInsert:
            node.next = prev.next
            prev.next = node
        
        return head

    # Solving it again - day 2
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        # Create the node anyways
        node = Node(insertVal, None)
        
        # if head is None
        if head is None:
            head = node
            head.next = head
            return head
        
        prev = head
        current = head.next
        inserted = False
        while prev.next != head:
            if insertVal >= prev.val and insertVal <= current.val:
                node.next = current
                prev.next = node
                inserted = True
                break
            elif prev.val > current.val and insertVal >= prev.val:                
                node.next = current
                prev.next = node
                inserted = True
                break
            elif prev.val > current.val and insertVal <= current.val:                
                node.next = current
                prev.next = node
                inserted = True
                break
                
            prev = prev.next
            current = current.next
            
        if not inserted:
            node.next = current
            prev.next = node
        
        return head