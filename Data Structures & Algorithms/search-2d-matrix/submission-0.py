class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, btm = 0, ROWS - 1

        while top <= btm:
            m = (btm + top) // 2

            if matrix[m][0] > target:
                btm = m - 1
            elif matrix[m][-1] < target:
                top = m + 1 
            else: # Row found
                break 
        
        # didnt find row, finished full cycle:
        if top > btm:
            return False
        
        row = (top + btm) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1   
            else:
                return True

        return False