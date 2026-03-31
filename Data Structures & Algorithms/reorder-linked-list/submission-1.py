# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev
        first = head
        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second = temp2
            first.next.next = temp1
            first = temp1


        