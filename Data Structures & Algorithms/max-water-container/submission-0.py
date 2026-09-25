class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            width = (r - l)  # distance between two pillars
            height = min(heights[l], heights[r])  # need to pick min since otherwise the water would leak
            max_area = max(max_area, (width * height))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
        