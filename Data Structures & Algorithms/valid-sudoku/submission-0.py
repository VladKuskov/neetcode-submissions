class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # no repeating values per row or column
        # no duplicates allowed each 3x3 box
        seen = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                row_key = (num, r, "row")
                col_key = (num, c, "col")
                box_key = (num, r//3, c//3, "box")
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True