class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = 0
        m = nums[0]
        for i in nums:
            cs = max(cs+i,i)
            m = max(cs,m)
            
        return m