class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            max_area = max(max_area, area)

            if heights[i] <= height:
                i += 1
            else:
                j -=1

        return max_area