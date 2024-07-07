class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target <= nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        for x in range (1, len(nums)):
            if nums[x-1] <= target and target <= nums[x]:
                return x
        return 0
