# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        head=ListNode(0,None)
        curr=head
        carry=0
        while curr1 or curr2:
            if not curr1:
                t1=0
            else:
                t1=curr1.val
            if not curr2:
                t2=0
            else:
                t2=curr2.val
            amt=t1+t2+carry
            carry=(t1+t2+carry)//10
            amt=amt%10
            curr.next=ListNode(amt)
            curr=curr.next
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        if carry:
            curr.next=ListNode(carry,None)
        return head.next
