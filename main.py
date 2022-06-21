#Steps
# 1.Get input from user
# 2.Print out the input problem.
# 3.Iterate over each element in the array(s)
# 4.Starting from 1 check if any of the nums upto 9 can be filled in there. If yes,probably go to the next
# iteration while remembering the location of the current element.
# 5.Repeat the process until you can no longer find an element that fits the location, in that case
# you wanna go to the previous location(back track and put in some other element there).


import time
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
def disp_board():
    for i in range(9):
        print()
        if i!=0 and i%3==0:
            print('-------------------')
        for j in range(9):
            if j!=0 and j%3==0:
                print('|',end=' ')
            print(board[i][j],end=' ')

def find_empty():
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)     # row,col
    return (-1,-1)

def is_valid(num,row,col):
    # print("Inside is_valid function")
    #check row
    for i in range(9):
        if i!=col and num==board[row][i]:
            return False
    #check col
    for i in range(9):
        if i!=row and num==board[i][col]:
            return False


    for i in range(row//3*3,row//3*3+3):
        for j in range(col//3*3,col//3*3+3):
            if (i,j)!=(row,col) and board[i][j]==num:
                return False

    return True





def solve_board():
    row=find_empty()[0]
    col=find_empty()[1]
    stack=[]
    while True:
        if row==-1:
            return True
        flag=False
        for n in range(board[row][col]+1,10):
            if is_valid(n,row,col)==True:
                board[row][col]=n
                stack.append((row,col))
                # print(stack)
                flag=True
                break

        if flag==True:
            row=find_empty()[0]
            col=find_empty()[1]
        else:
            #backtracking steps
            board[row][col] = 0
            pos=stack.pop()
            row=pos[0]
            col=pos[1]


#the above function can also be implemented recursively!!(without stacks)









disp_board()
print()
print("Solving...")
time.sleep(5)
print("Solved!!!")
print()
solve_board()

disp_board()

disp_board()