import collections

class Solution:
    def isValidSudoku(self, board, List[List[str]]) -> bool:
        # To solve this problem, we have to understand that there can be no duplicates in ROWS, COLS, and 3 x 3 SQUARES within the 9 x 9 GRID.
        
        # WE can use hashsets to check for duplicates and then hashmaps that do not raise key errors to store those values we loop through to a key such as cols
        
        # WE use integer division because the numbers in 3 x 3 grids can be looked at as coordinates in sets of three, so out of three integers which one are they, and then once dividing 4 // 3, we get 1 which is the second box giving the program a location to look at, etc
        
        rows = collections.defaultdict(set) # KEY = (r , c)
        cols = collections.defaultdict(set) # KEY = (r , c)
        squares = collections.defaultdict(set) # KEY = (r / 3 , c / 3)
        
        # Since we know the prompt is giving us a 9 x 9 board, we can set the for loop to a range of 9, and we will use a nested for loop because we are using two arrays, c and r, to check the entire board
        for r in range(9):
            for c in range(9):
                # If to make sure '.' is passed through
                if board[r][c] == '.':
                    continue
                # If to check if duplicates, dont forget or
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r // 3, c // 3] 
                ):
                    return False
                # if the number we are looking at are not duplicates values, we add them to the hashmap to create a lookup table
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])
        # Return true if the loops have not determined any duplicates in their hashmaps
        return True