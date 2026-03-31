# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # First step to get the mid point of the Linkd List
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        second=s.next
        s.next=None
        first=head

        #Second step is to reverse the second list
        prev=None
        curr=second
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        second=prev

        #Third step is to merge first and second linked lists
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
