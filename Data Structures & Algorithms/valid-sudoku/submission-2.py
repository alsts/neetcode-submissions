class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board)):
                cell = board[r][c]

                if cell != '.':
                    if cell in rows[r] or cell in cols[c] or cell in boxes[r // 3][c // 3]:
                        return False
                    else:
                        rows[r].add(cell)
                        cols[c].add(cell)
                        boxes[r // 3][c // 3].add(cell)

        return True
        