class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = set(numbers)

        for i in range(len(numbers)):
            if numbers[i] > target:
                return []
            
            complement = target - numbers[i]
            if complement in nums:
                return [i+1, numbers.index(complement)+1]

        return []