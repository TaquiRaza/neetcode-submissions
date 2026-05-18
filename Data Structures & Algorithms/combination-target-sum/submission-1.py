class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()

        answer = []
        curr = []

        def backtrack(i, curr, answer):
            total = sum(curr)
            if total == target:
                answer.append(curr.copy())
                return True

            if total > target:
                return False

            if i == len(nums):
                return False
            
            # try repeating the same number
            curr.append(nums[i])
            backtrack(i, curr, answer)
            curr.pop()

            # try skipping the current number
            backtrack(i+1, curr, answer)
        
        backtrack(0, curr, answer)

        return answer