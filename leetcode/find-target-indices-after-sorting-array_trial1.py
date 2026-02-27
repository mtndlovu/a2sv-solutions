class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        targets = [i for i in range(len(nums)) if nums[i] == target]
        return targets