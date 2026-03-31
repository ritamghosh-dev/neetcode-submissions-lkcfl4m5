# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack=[]
        curr=head
        while curr:
            stack.append(curr.val)
            curr=curr.next
        head=ListNode(stack.pop())
        curr=head
        while stack:
            newNode=ListNode(stack.pop())
            curr.next=newNode
            curr=newNode
        return head

