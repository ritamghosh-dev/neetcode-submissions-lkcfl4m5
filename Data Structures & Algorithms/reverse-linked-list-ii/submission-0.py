# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right==left:
            return head
        dummy = ListNode(next=head)
        before = dummy
        for i in range(left-1):
            before = before.next
        after = dummy
        for i in range(right):
            after = after.next
        end = after
        after = after.next
        start = before.next
        prev = None
        curr = before.next
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        if before == dummy:
            head = end
        else:
            before.next = end
        if after:
            start.next = after
        return head

        
        

