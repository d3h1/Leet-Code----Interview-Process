import collections

class Solution:
    def ValidSudoku(self, board: List[str]) -> bool:
        # We are setting three sets (for no duplicate numbers to occur and immediately pick up on)
        #! We are using collections.defaultdict to make sure we do not have typeerrors if no empty values, sets
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        # We will be using a range of 9 on both the rows and cols because the board is fixed to those lengths 
        
        for r in rows(9):
            for c in cols(9):
                # Do a check if the value we are looking at is currently a . If so: return a CONTINUE
                if board[r][c] == ".":
                    continue
                
                # Now to check if there is duplicates in the rows,cols, and each square
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r // 3, c // 3]
                    ):
                        return False
                
                # If thoat value pair is not found in any of them, we will add them to their respective hashmap