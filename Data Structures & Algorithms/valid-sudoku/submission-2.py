class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Was accidentally trying to create my own board

        # List of numeric digits
        #List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Board row index
        # board[i]
        # Board column index
        # board[j]
        #new_array = []
        #for k in range(len(List)):
            #new_array = [List[k].rand()] * 3
        #for i in range (len(board)/3):
            #for j in range (len(board[i])/3):

        # Loop through the input board
        #row = 0
        #column = 0
        #for row in range(len(board)):
            #if(board[row+1] == board[row]):
                #return True
            #else:
                #return False
        #for column in range(len(board[row])):
            ##   return True
            #else:
             #   return False

        # Use hash maps for rows, columns and squares
        #rowhashmap = map(row)
        #columnhashmap = map(column)
        #squareshashmap = map(square)

        # Square design and index of each square
        #sqaure = [(len(board[row])/3) * len(board[column]/3)]
        #square[index] = (row/3) *3 + (col/3)

        #for index in square:
            # Extra last minute logic to check for duplicates
            #if(square[index] == square[index+1]):
                #return False
            #else:
                #return True
        #if rowhasmap == columnhashmap:
            #return False
        #else: 
            #return True  


    # Correct Solution Hash Set/Dictionary wise
        # Hashmap
        # Key = Column/row/square #
        # Set represents all particular values in the column/row/square
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        # Loop through 9 rows and columns
        for r in range(9):
            for c in range(9):
                # If the position in the board is empty ("."), then we can just skip
                # the position and go to the next iteration of the loop
                if board[r][c] == ".":
                    continue
                # Trying to find a duplicate. Rows = hashmap, key = value we're putting in
                # rows[r] = hashset of all particular values that occur in this particular row#
                # Rows = hashmap
                # Checking if the current number that we have is already inside this current row
                # then it is a duplicate and we return false
                # Same logic for columns if value has occured in the current column that we are in
                # (r//3 and c//3) tells us which current square we're in
                # board[r][c] in squares[(r//3, c//3) returns a set of all the values that we have seen in the current square before
                # if the value we're at is a duplicate, then its gonna already be inside the hashset and we return False
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                # If sudoku is valid, we update the hashmaps up above and add the current value/character to the board
                # For each row, column and square
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
            # If we never detect any duplicates as we loop through the entire board's rows, columns and squares
            # Then we return True and the sudoku board is valid
        return True