class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            if target - num in nums:
                j = nums.index(target - num)
                if i != j:
                    break
            else:
                continue
            
        return [i, j]