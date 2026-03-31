class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tracker = Counter(nums)
        for key in tracker:
            if tracker[key]>1:
                return key