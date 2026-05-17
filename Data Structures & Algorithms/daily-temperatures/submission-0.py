class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = [] # [temp, index]

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                temp, ind = stack.pop()
                result[ind] = i - ind
            stack.append([n, i])

        return result