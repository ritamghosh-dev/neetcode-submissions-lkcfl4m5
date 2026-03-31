class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(0,n-2):
            l=i+1
            r=n-1
            while l<r:
                if nums[l]+nums[r]==-nums[i]:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[l]+nums[r]>-nums[i]:
                    r-=1
                else:
                    l+=1
        return ans

