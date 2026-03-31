class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker={}
        for word in strs:
            key=''.join(sorted(list(word)))
            if key in tracker:
                tracker[key].append(word)
            else:
                tracker[key]=[word]
        return tracker.values()