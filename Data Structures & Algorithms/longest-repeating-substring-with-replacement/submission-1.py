class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = float(0)
        l = 0
        curr = collections.defaultdict(int)
        for r in range(len(s)):
            curr[s[r]]+=1
            while (r-l+1) - max(curr.values()) > k:
                curr[s[l]]-=1
                l+=1
            ans = max(ans, r - l + 1)
        return ans

                

        #     if curr and curr != s[r]:
        #         k -= 1
        #         while k < 0:
        #             if s[l] != curr:
        #                 k+=1
        #                 l+=1
        #                 break
        #             l+=1
        #     elif not curr:

                
        #     ans = max(ans, r - l +1)
        # return ans
                    