class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0]<nums[1] and nums[0]<nums[-1]:
            return nums[0]
        l=0
        r=n-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[(mid+1)%n]>nums[mid] and nums[(mid-1)%n]>nums[mid]:
                return nums[mid%n]
            elif nums[(mid+1)%n]<nums[mid]:
                return nums[(mid+1)%n]
            elif abs(nums[l]-nums[mid])>abs(nums[r]-nums[mid]):
                r=mid
            else:
                l=mid+1
