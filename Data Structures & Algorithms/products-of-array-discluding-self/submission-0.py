class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_res = []
        prefix_product = 1

        for i in range(len(nums)):
            prefix_product *= nums[i]
            prefix_res.append(prefix_product)

        postfix_res = [0] * len(nums)
        postfix_product = 1

        for i in range(len(nums) - 1, -1, -1):
            postfix_product *= nums[i]
            postfix_res[i] = postfix_product

        result = []
        for i in range(len(nums)):
            # prefix and postfix of value
            prefix = prefix_res[i - 1] if i > 0 else 1
            postfix = postfix_res[i + 1] if i + 1 < len(nums) else 1

            result.append(prefix * postfix)

        return result   