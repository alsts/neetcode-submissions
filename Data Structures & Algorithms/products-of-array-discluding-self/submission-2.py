class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # build prefix product array
        for i in range(0, len(nums)):
            result[i] = (result[i - 1] if i > 0 else 1) * nums[i]

        # build postfix product array
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = (result[i - 1] if i > 0 else 1) * postfix
            postfix *= nums[i]

        return result