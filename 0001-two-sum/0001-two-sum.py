class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indexes = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indexes:
                return [num_indexes[complement], i]
            num_indexes[num] = i

        return []
