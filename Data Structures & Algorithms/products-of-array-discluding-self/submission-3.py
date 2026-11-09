class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_res = []
        prefix_product = 1
        for i in range(len(nums)):
            prefix_product *= nums[i]
            prefix_res.append(prefix_product)

        postfix_res = [1] * len(nums)
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_product *= nums[i]
            postfix_res[i] = postfix_product

        res = []
        for i in range(len(nums)):
            prefix_i = prefix_res[i-1] if i > 0 else 1
            postfix_i = postfix_res[i+1] if i + 1 < len(nums) else 1    
            res.append(prefix_i * postfix_i)

        return res