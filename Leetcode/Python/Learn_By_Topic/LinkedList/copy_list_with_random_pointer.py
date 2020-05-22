# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    
    # Using Hashmap - Tn = O(N) Sn = O(N)
    def __init__(self):
        self.visitedHashMap = {}
    
    def getClonedList(self, node):
        if node:
            if node in self.visitedHashMap.keys():
                return self.visitedHashMap[node]
            else:
                self.visitedHashMap[node] = Node(node.val, None, None)
                return self.visitedHashMap[node]
        else:
            return None
    
    def copyRandomList_ONON(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        old_node = head
        new_node = Node(old_node.val, None, None)
        new_head = new_node        
        self.visitedHashMap[old_node] = new_node
        
        while old_node:
            new_node.random = self.getClonedList(old_node.random)
            new_node.next = self.getClonedList(old_node.next)
            
            old_node = old_node.next
            new_node = new_node.next
            
        return new_head
    
    # Using List only - Tn = O(N) Sn = O(1)
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        # Create new list and place nodes in between old list nodes
        current = head
        while current:
            new_node = Node(current.val, None, None)
            new_node.next = current.next          
            current.next = new_node
            current = new_node.next
            
        # Update random pointers for new list nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            else:
                current.next.random = None
                
            current = current.next.next
            
        # Separate both list
        print(head.val)
        old_node = head
        new_node = head.next
        new_head = head.next
        while old_node:
            old_node.next = old_node.next.next
            old_node = new_node.next
            
            if new_node.next:
                new_node.next = new_node.next.next
            else:
                new_node.next = None
            new_node = new_node.next
            
        return new_head
        