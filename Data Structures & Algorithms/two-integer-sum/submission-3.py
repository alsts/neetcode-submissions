class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, n in enumerate(nums):
            other_num = target - n
            if other_num in visited:
                return [visited[other_num], i]
            visited[n] = i

        return []