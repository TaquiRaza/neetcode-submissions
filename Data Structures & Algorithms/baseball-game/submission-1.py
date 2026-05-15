class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op.isnumeric() or op[1:].isnumeric():
                scores.append(int(op))
            elif op == "+":
                scores.append(scores[-1]+scores[-2])
            elif op == "D":
                scores.append(2*scores[-1])
            elif op == "C":
                scores.pop()
        return sum(scores)