class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.'] * n for _ in range(n)]

        rows = set()
        cols = set()
        diagonal1 = set() # abs(r - c)
        diagonal2 = set() # r + c

        result = []
        
        def backtrack(r):
            if r == n:
                result.append(["".join(row) for row in grid])
                return
            
            for c in range(n):
                if r in rows or c in cols or r-c in diagonal1 or r+c in diagonal2:
                    continue
                rows.add(r)
                cols.add(c)
                diagonal1.add(r-c)
                diagonal2.add(r+c)
                grid[r][c] = 'Q'
                backtrack(r+1)
                grid[r][c] = '.'
                rows.remove(r)
                cols.remove(c)
                diagonal1.remove(r-c)
                diagonal2.remove(r+c)


        backtrack(0)
        return result