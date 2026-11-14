class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_pillar, r_pillar = height[l], height[r]
        water = 0

        while l < r:
            if height[l] < height[r]: # left pillar dictates water level
                l += 1
                if l_pillar > height[l]: # inner pillar smaller -> water
                    water += l_pillar - height[l]
                else:
                    l_pillar = height[l]
            else:
                r -= 1   
                if r_pillar > height[r]: # inner pillar smaller -> water
                    water += r_pillar - height[r]
                else:
                    r_pillar = height[r]  

        return water