class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        if n>len(s2):
            return False
        s1=Counter(s1)
        tracker=collections.defaultdict(int)
        for i in range(n-1):
            tracker[s2[i]]+=1
        l=0
        for r in range(n-1,len(s2)):
            tracker[s2[r]]+=1
            temp=True
            for key in s1.keys():
                if s1[key]!=tracker[key]:
                    temp=False
                    break
            if temp:
                return True
            tracker[s2[l]]-=1
            l+=1

            
        return False

