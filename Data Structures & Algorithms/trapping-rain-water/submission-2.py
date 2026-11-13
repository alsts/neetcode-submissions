class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_wall, right_wall = height[l], height[r]   # tallest seen so far on each side
        water = 0

        while l < r:
            if left_wall < right_wall:          # left wall is lower → it decides the water level
                l += 1
                pillar = height[l]
                if pillar >= left_wall:
                    left_wall = pillar           # new taller wall, no water on top of it
                else:
                    water += left_wall - pillar  # lower than the wall → water fills the gap
            else:                               # right wall is lower (or equal) → it decides
                r -= 1
                pillar = height[r]
                if pillar >= right_wall:
                    right_wall = pillar
                else:
                    water += right_wall - pillar

        return water