from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        clm = defaultdict(set)
        b = defaultdict(set)

        for r in range(1,10):
            for c in range(1,10):
                v = board[r-1][c-1]
                if board[r-1][c-1] == '.':
                    continue
                b_id = ((r-1)//3,(c-1)//3)
                if v in row[r] or v in clm[c] or v in b[b_id]:
                    return False
                row[r].add(board[r-1][c-1])
                clm[c].add(board[r-1][c-1])
                b[b_id].add(board[r-1][c-1])
        
        return True