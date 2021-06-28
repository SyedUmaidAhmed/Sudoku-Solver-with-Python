# This is the Sudoku Puzzle It consists of 9 lists inside
# Always Remember the
#"ONE COMPLETE LIST [] IS ONE ELEMENT"
# So there are 9 elements in total, IF you consider only one list
# THERE are also 9 elements

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board1 = [
    [0,0,0,5,2,0,0,0,9],
    [0,2,0,0,2,8,0,3,0],
    [0,0,0,0,0,0,4,7,0],
    [0,0,0,0,3,4,0,0,0],
    [0,8,0,6,0,2,0,0,0],
    [4,6,0,0,7,1,0,0,0],
    [1,4,0,0,0,0,0,0,6],
    [0,0,0,0,0,7,0,2,0],
    [7,0,0,0,0,0,0,9,0]
]


board2 = [
    [0,0,7,0,0,0,5,0,8],
    [0,0,4,3,8,0,0,2,0],
    [0,0,0,7,0,0,0,0,0],
    [0,2,0,0,6,0,0,0,9],
    [1,0,5,0,0,0,0,0,7],
    [0,0,0,9,3,0,0,5,0],
    [0,0,0,0,4,0,3,0,0],
    [0,8,0,6,0,0,0,0,0],
    [5,6,0,0,0,9,0,0,0]
]









#print(len(board))


def solve(bo):

    find = find_empty(bo)

    if not find:
        return True
    else:
        row,col = find


    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo,num,pos):

# CHECK ROW AND COLUMN IN 2 FOR LOOPS
    
    for i in range(len(bo)):
        if bo[pos[0]][i]==num:
            return False

    for i in range(len(bo[0])):
        if bo[i][pos[1]]==num:
            return False

    # CHECK BOX
    box_x = pos[0]//3
    box_y = pos[1]//3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if bo[i][j]==num:
                return False

    return True








def print_board(bo):  #FUNCTION

# Each list (one square bracket) count the row number
# That's why used "len(bo)"

    for i in range(len(bo)):   ##Because see the ROW number

        if i%3==0 and i!=0:
            print("- - - - - - - - - - -")

# But in J we used len(bo[0])
# means that we are using column , See column marks inside the list 1st Element

        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print("| ", end="")
                
# Change line after 8 elements

            if j==8:
                print(bo[i][j])

#Print space after each element, if not on last entry
#Don't spare the line
                
            else:
                print(str(bo[i][j])+" ",end="")



def find_empty(bo):
    for i in range(len(bo)):  # Same we write for ROW number
        for j in range(len(bo[0])):   # Same we write for column number
            if bo[i][j]==0:
                return(i,j)
    return None



print_board(board)
solve(board)
print("\n________________________\n\n")
print_board(board)

            
