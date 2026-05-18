class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        visit = set()

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == -1:
                    visit.add((r,c))
                if cell == 0:
                    q.append((r,c))
                    visit.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if r+dr >= len(grid) or c+dc >= len(grid[0]) or r+dr<0 or c+dc<0:
                        continue
                    if (r+dr, c+dc) in visit:
                        continue
                    if grid[r+dr][c+dc] == -1:
                        continue
                    q.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))
            dist += 1
        