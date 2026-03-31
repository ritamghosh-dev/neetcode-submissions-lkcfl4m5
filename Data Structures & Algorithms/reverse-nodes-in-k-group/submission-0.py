# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fakeHead=ListNode()
        fakeHead.next=head
        before=fakeHead
        after=None
        curr=head
        while before:
            i=0
            stack=[]
            while i<k:
                if not curr:
                    return fakeHead.next
                stack.append(curr.val)
                i+=1
                curr=curr.next
            after=curr
            while stack:
                newNode=ListNode(stack.pop())
                before.next=newNode
                before=newNode
            before.next=after
        return fakeHead.next


             

        