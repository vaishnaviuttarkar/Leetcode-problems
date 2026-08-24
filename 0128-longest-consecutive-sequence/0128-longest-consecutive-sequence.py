class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        if len(s)==0: return 0 
        if len(s)==1: return 1
        longest = 0
        for i in s:
            if i-1 not in s:
                current = i
                length = 1

                while current+1 in s:
                    current += 1
                    length += 1

                    longest = max(length,longest)
                    
                longest = max(length,longest)
                    
        return longest