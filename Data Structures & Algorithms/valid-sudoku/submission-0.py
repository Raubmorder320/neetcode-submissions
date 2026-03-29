class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set(),9:set()}
        clm = {1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set(),9:set()}
        b = {(0,0):set(),(0,1):set(),(0,2):set(),(1,0):set(),(1,1):set(),(1,2):set(),(2,0):set(),(2,1):set(),(2,2):set()}

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