class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    continue
                if x in rows[i]:
                    return False
                rows[i].add(x)
                if x in cols[j]:
                    return False
                cols[j].add(x)
                box_i = i // 3
                box_j = j // 3
                if x in boxes[(box_i, box_j)]:
                    return False
                boxes[(box_i, box_j)].add(x)
        return True