class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = set(nums)
        maxlen = 0

        for n in nums:
            length = 0
            while n in seqs:
                length += 1
                maxlen = max(maxlen, length)
                n -= 1
        
        return maxlen