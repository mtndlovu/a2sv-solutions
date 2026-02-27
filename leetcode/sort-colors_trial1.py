class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        sorted_idx, check_idx = 0, 1

        while n > 1 and check_idx < n:
            if nums[sorted_idx] > nums[check_idx]:
                nums[sorted_idx], nums[check_idx] = nums[check_idx], nums[sorted_idx]
                sorted_idx, check_idx = check_idx, sorted_idx
                while check_idx > 0 and nums[check_idx] < nums[check_idx - 1]:
                    nums[check_idx], nums[check_idx - 1] = nums[check_idx - 1], nums[check_idx]
                    check_idx -= 1
                check_idx = sorted_idx + 1
            else:
                sorted_idx += 1
                check_idx += 1