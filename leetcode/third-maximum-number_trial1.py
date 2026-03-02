class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        unique = [nums[0]]

        if n < 3:
            return max(nums)

        for i in range(1, n):
            if not unique or nums[i-1] != nums[i]:
                unique.append(nums[i])

        if len(unique) < 3:
            return max(unique)
        else:
            return unique[-3]