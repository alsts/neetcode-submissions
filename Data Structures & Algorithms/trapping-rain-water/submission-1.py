class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        while l < r:
            if left_max < right_max: # lower wall decides (water spills)
                l += 1
                left_max = max(left_max, height[l]) # old pillar vs inner
                res += left_max - height[l] # old pillar higher -> diff -> water
            else:
                r -= 1
                right_max = max(right_max, height[r]) # old pillar vs inner
                res += right_max - height[r] # old pillar higher -> diff -> water

        return res
        