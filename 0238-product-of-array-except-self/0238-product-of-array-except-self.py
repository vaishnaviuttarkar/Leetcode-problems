import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_max= math.prod(nums)
        new = []
        
        for n,i in enumerate(nums):
            if i == 0:
                new.append(math.prod(nums[:n])*math.prod(nums[n+1:]))
            else:
                new.append(all_max//i)

        return new