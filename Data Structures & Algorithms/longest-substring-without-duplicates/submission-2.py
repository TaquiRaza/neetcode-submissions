class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left, maxlen = 0, 0
        loc = {}

        for i, c in enumerate(s):
            if c in loc:
                left = max(left, loc[c] + 1)
            maxlen = max(maxlen, i - left + 1)
            loc[c] = i
        
        return maxlen