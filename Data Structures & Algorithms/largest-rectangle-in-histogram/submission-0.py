class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [height, index]
        maxarea = 0

        for i, h in enumerate(heights):
            right = i
            while stack and stack[-1][0] > h:
                prev_height, prev_ind = stack.pop()
                maxarea = max(maxarea, prev_height * (i-prev_ind))
                right = prev_ind
            stack.append([h, right])
        
        i = len(heights)
        while stack:
            prev_height, prev_ind = stack.pop()
            maxarea = max(maxarea, prev_height * (i-prev_ind))

        return maxarea