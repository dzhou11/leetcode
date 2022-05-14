"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    """
    do not use queue, setup "next" link for the next level and move down
    time: n 
    Space: 1
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr=root
        dummy = Node(1)
        head = root
        
        while head:
            
            curr = head
            prev = dummy
            
            while curr: # one level
                if curr.left:
                    prev.next = curr.left
                    prev = curr.left
                if curr.right:
                    prev.next = curr.right
                    prev = curr.right
                curr = curr.next
            head = dummy.next
            dummy.next = None
        return root
    """
    def connect(self, root: 'Node') -> 'Node':
    
    # use a queue to do breadth first search
    # time n, space n 
        if not root:
            return
        q = deque()
        q.append(root)
        
        dummy = Node(-1)
        while q: 
            #[print(i.val) for i in q]
            #print('----')
            prev = dummy 
            length = len(q)
            for _ in range(length):
                popped = q.popleft()
                #print("pop:",popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                prev.next = popped
                prev = popped
        return root
    """
            
