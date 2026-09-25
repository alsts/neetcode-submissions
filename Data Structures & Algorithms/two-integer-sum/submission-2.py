class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_vals = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in prev_vals:
                return [prev_vals[diff], i]
            prev_vals[nums[i]] = i
