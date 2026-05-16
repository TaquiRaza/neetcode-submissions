class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxleft, maxright = 0, 0
        total = 0

        curr = l

        while l < r:
            total += max(0, min(maxleft, maxright) - height[curr])
            maxleft = max(maxleft, height[l])
            maxright = max(maxright, height[r])

            if maxleft <= maxright:
                l += 1
                curr = l
            else:
                r -= 1
                curr = r
        
        return total