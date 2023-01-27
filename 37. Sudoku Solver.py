class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board,r,c,val):
            for i in range(9):
                if board[i][c] == val or board[r][i] == val or board[3*(r//3) + i//3][3*(c//3) + i%3] == val:
                    return False
            return True
        def solve(board):    
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for val in range(1,10):
                            if isValid(board,r,c,str(val)):
                                board[r][c] = str(val)
                                
                                if solve(board) == True:
                                    return True
                                else:
                                    board[r][c] = '.'
                        return False
            return True
        solve(board)
        
                
                            
                         
        
            