class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            t1 = numbers[left]+numbers[right] 
            if t1>target:
                right -= 1
            elif t1<target:
                left += 1
            else:
                return [left+1,right+1]
        