import collections
def isValidSudoku(board: list[list[str]]) -> bool:
    row = set()
    col = set()
    subgrid = set()

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if ((r, board[r][c]) in row or 
                (c, board[r][c]) in col or 
                (r//3, c//3, board[r][c]) in subgrid):
                return False
            
            row.add((r, board[r][c]))
            col.add((c, board[r][c]))
            subgrid.add((r//3, c//3, board[r][c]))
    return True

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], 
         ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
         [".", "9", "8", ".", ".", ".", ".", "6", "."], 
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
         [".", "6", ".", ".", ".", ".", "2", "8", "."], 
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))