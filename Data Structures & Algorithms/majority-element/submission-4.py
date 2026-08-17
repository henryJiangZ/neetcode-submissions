class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if not num in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        return max(seen, key = seen.get)