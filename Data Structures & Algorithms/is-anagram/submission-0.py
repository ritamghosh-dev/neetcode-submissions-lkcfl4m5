class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_track=Counter(s)
        t_track=Counter(t) 
        if s_track==t_track:
            return True
        else:
            return False