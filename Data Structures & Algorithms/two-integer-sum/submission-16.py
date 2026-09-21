class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in enumerate(nums):
            if j not in seen:
                seen[j] = i
            diff = target - j
            if diff in seen and i != seen[diff]:
                return [seen[diff],i]