class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        for item in nums:
            if item-1 not in nums:
                length=0
                while item+length in nums:
                    length+=1
                ans=max(ans,length)  
        return ans