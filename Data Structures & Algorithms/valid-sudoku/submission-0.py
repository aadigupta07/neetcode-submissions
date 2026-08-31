class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                box = (i // 3) * 3 + j // 3
                curr1 = f"{val} in box {box}"
                curr2 = f"{val} in row {i}"
                curr3 = f"{val} in col {j}"
                if curr1 in seen or curr2 in seen or curr3 in seen:
                    return False
                
                seen.add(curr1)
                seen.add(curr2)
                seen.add(curr3)
        
        return True