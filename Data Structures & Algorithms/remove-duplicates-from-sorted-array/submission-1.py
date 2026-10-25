class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] < nums[slow]:
                return len(nums[0:slow+1])
            elif nums[slow] == nums[fast]:
                fast += 1
            else:
                slow+=1
                nums[slow] = nums[fast]
        return len(nums[0:slow+1])