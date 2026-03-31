# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            mergedLists=[]
            for i in range(0,len(lists),2):
                if i+1>=len(lists):
                    l2=None
                else:
                    l2=lists[i+1]
                mergedLists.append(self.merge2Lists(lists[i],l2))
            lists=mergedLists
        return lists[0]


    def merge2Lists(self,l1,l2):
        fakeHead=ListNode()
        curr=fakeHead
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        if l1:
            curr.next=l1
        elif l2:
            curr.next=l2
        return fakeHead.next