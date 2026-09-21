class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,value in enumerate(nums):
            if value not in seen:
                seen[value] = index
            diff = target-value
            if diff in seen and seen[diff]!=index:
                return [seen[diff],index]