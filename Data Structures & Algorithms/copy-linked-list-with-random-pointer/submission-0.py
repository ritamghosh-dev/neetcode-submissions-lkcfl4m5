"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        duplicate={}
        curr=head
        while curr:
            duplicate[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr and curr.next:
            duplicate[curr].next=duplicate[curr.next]
            curr=curr.next
        curr=head
        while curr:
            if curr.random:
                duplicate[curr].random=duplicate[curr.random]
            curr=curr.next
        return duplicate[head]
        