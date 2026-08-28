class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if (f"row {i+1}", num) in seen:
                    return False
                if (f"column {j+1}", num) in seen:
                    return False
                if (f"box {(i//3 * 3 + j//3) + 1}", num) in seen:
                    return False
                
                seen.add((f"row {i+1}", num))
                seen.add((f"column {j+1}", num))
                seen.add((f"box {(i//3 * 3 + j//3) + 1}", num))
        
        return True
