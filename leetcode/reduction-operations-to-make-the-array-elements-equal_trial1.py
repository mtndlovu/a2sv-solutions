class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        curr, ops = nums[0], 0
        increment = 0

        for i in range(1, len(nums)):
            if curr != nums[i]:
                increment += 1
                ops += increment
            else:
                ops += increment
            
            curr = nums[i]
        
        return ops