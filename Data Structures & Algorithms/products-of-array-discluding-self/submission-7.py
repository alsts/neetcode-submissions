class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i] # lag one step

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix # apply here
            postfix *= nums[i] # lag one step

        return products

