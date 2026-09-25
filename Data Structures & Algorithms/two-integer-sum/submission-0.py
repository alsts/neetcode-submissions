class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset[nums[i]] = i

            j = target - nums[i]
            if j in hashset and hashset[j] != i:
                return [hashset[j], i]
        