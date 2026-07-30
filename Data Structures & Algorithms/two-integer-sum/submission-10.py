class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in nums: 
            needed = target - i
            if needed == i and needed in seen:
                return [nums.index(i),nums.index(i,(nums.index(i))+1,len(nums))]
            elif needed in seen:
                return [nums.index(needed),nums.index(i)]
            seen[i] = nums.index(i)
