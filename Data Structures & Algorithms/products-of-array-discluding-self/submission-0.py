class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        n=len(nums)
        for i in range(1,n):
            prefix.append(nums[i-1]*prefix[i-1])
        suffix=[1]
        curr=1
        for i in range(n-2,-1,-1):
            curr=curr*nums[i+1]
            suffix.insert(0,curr)
        ans=[]
        for i in range(n):
            ans.append(prefix[i]*suffix[i])
        return ans