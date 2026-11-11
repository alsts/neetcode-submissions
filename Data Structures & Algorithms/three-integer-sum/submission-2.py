class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):

            # would never sum up to 0 (in sorted) [-2,-1,[1],2,3]
            if num > 0: 
                break

            # duplicate
            if i > 0 and num == nums[i-1]:
                continue    

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1 # # ← this line skips the right-side duplicates
                elif three_sum < 0:
                    l += 1
                else:
                    # sum found, continue to next numbers
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # required: skip duplicate left values, otherwise the same triplet is added twice [-2, -1, [-1],1,1,2,4]
                    while l < r and nums[l] == nums[l - 1]: # l - 1 is just added sum to result
                        l += 1 


        return result            