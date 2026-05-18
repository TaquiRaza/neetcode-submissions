class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr = []

        def backtrack(i, subsets, curr):
            if i == len(nums):
                subsets.append(curr.copy())
                return
            
            backtrack(i+1, subsets, curr)
            curr.append(nums[i])
            
            backtrack(i+1, subsets, curr)
            curr.pop()

        backtrack(0, subsets, curr)
        
        return subsets