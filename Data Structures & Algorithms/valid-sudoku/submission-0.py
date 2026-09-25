class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(len(board))]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            row = set()

            for c in range(len(board)):
                cell = board[r][c]

                if cell != '.':
                    box_r = math.ceil((r + 1) / 3) - 1
                    box_c = math.ceil((c + 1) / 3) - 1

                    if cell in row or cell in cols[c] or cell in boxes[box_r][box_c]:
                        return False
                    else:
                        row.add(cell)
                        cols[c].add(cell)
                        boxes[box_r][box_c].add(cell)

        return True
        