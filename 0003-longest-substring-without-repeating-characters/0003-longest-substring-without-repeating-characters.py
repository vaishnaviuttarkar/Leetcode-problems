class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        L = 0
        R = 0
        seen = set()
        while (R)!=len(s):
            if s[R] in seen:
                seen.remove(s[L])
                L += 1
            else:
                seen.add(s[R])
                R += 1
            longest = max(longest,len(seen))
        return longest