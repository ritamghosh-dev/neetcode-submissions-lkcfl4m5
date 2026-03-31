class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=len(nums1)+len(nums2)
        half=(total+1)//2 #To make sure in odd case left side has more elements, because we return max of left in that case
        a=nums1
        b=nums2
        if len(a)>len(b):
            a,b=nums2,nums1
        l=0
        r=len(a)  
        while l<=r:
            mid1=(l+r)//2
            mid2=half-mid1
            if mid1-1>=0:
                l1=a[mid1-1]
            else:
                l1=float('-inf')
            if mid2-1>=0:
                l2=b[mid2-1]
            else:
                l2=float('-inf')
            if mid1<len(a):
                r1=a[mid1]
            else:
                r1=float('inf')
            if mid2<len(b):
                r2=b[mid2]
            else:
                r2=float('inf')    
            if l1<=r2 and l2<=r1:
                if total%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            elif l1>r2:
                r=mid1-1
            else:
                l=mid1+1
                   
