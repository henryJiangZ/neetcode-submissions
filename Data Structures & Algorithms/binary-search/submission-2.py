class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = low + (high-low)//2
            if(nums[mid]==target):
                return mid
            if(nums[mid] > target):
                high = mid-1
                self.search(nums[low:high],target)
            else:
                low = mid+1
                self.search(nums[low:high],target)
        return -1