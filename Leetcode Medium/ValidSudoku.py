class Solution:
    def isValidSudoku(self, board, List[List[str]]) -> bool:
        # We have to first define each check needed to determine validity of the leetcode: COLS, ROWS, SQUARES
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = [(r // 3, c // 3)]
        
        for c in range(9):
            for r in range(9):
                if board[c][r] == '.':
                    continue
                if (board[c][r] in rows[r] or
                    board[c][r] in cols[c] or 
                    board[c][r] in squares[(r // 3, c // 3)]):
                    return False # Will return false if any step shows a duplicate in the previous keys
                
                # If the duplicate check passes, we will add the board[r][c] value to the key values
                rows[r].add(board[c][r])
                cols[c].add(board[c][r])
                squares[(r // 3, c // 3)].add(board[c][r])
        # Once the nested for loop finishes with no duplicate, we will get a successful return True
        return True