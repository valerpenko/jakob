def horse_step(row,col):
    global step_count
    step_count += 1
    board[row][col]=step_count

def show_board():
    for el in board:
        print(*el)
def next_move(row,col):
    shift=[[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
    for i in range(len(shift)):
        try:
            if board[row+shift[i][0]][col+shift[i][1]]==0:
                return row+shift[i][0],col+shift[i][1]
        except:
            pass
board=[[0 for i in range(8)]for i in range(8)]
r=0
c=0
step_count=0
while r>=0 and c>=0:
    horse_step(r,c)
    show_board()
    r,c=next_move(r,c)
    input()
