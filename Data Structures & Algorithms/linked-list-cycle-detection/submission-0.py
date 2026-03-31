# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if pos==-1:
            return False
        curr=head
        i=0
        temp=None
        while curr:
            if temp==curr:
                return True
            if i==pos:
                temp=curr 

            curr=curr.next
            i+=1
        return False