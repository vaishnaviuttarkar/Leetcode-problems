class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1

        seen1=sorted(seen, key=seen.get , reverse=True)
        return seen1[:k]

        
