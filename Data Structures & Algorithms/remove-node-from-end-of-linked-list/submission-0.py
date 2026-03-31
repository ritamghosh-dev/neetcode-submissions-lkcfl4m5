# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=1
        curr=head
        while curr:
            i+=1
            curr=curr.next
        target=i-n
        j=0
        prevHead=ListNode(-1,head)
        curr=prevHead
        while j<target-1:
            j+=1
            curr=curr.next
        curr.next=curr.next.next
        return prevHead.next

        
        