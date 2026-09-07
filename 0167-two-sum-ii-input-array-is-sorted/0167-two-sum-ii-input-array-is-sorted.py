class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        seen = {}
        for i,num in enumerate(numbers):
            competent = target - num
            if competent not in seen:
                seen[num] = i+1
            else:
                return [seen[competent],i+1]