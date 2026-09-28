class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            duplicate = nums[i]
            if duplicate in seen and abs(i-seen[duplicate]) <=k:
                return True;
            seen[nums[i]] = i
                    
        return False;
                