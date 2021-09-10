board=[]
CONTINUE=0
WIN_X=1
WIN_O=2
DRAW=3
EMPTY=0
X=1
O=2
move_count=0
turn_x=True #если флажок turn_x=False в масив добавляем "0" на указанные координаты если turn_x=True добовляем "X"
def init(n):
    global board
    board = [[0 for i in range(n)] for i in range(n)]
def get_board(row, col):
    return board[row][col]
def game_step(row, col):
    global turn_x
    global board
    global move_count

    if board[row][col]!=EMPTY:
        return
    board[row][col]=X if turn_x else O
    move_count+=1

def next_input():
    try:
        row, col = map(int, input("r,c:").split())
        return (row, col)
    except ValueError:
        pass

def game_status(row, col):
    global board
    global move_count
    global turn_x
    player=X if turn_x else O
    winer=WIN_X if turn_x else WIN_O

    # проверям вертикаль
    try:
        if board[row-2][col]==board[row-1][col] and board[row-1][col]==board[row][col]:
            return winer
        if board[row-1][col]==board[row][col] and board[row][col]==board[row+1][col]:
            return winer
        if board[row][col]==board[row+1][col] and board[row+1][col]==board[row+2][col]:
            return winer
    except(IndexError):
        ...

    # проверям столбцы
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return winer
    # проверям ДИАГОНАЛИ
    if board[0][0]==board[1][1]==board[2][2]==player or board[0][2]==board[1][1]==board[2][0]==player:
        return winer

    if move_count==100:
        return DRAW
    if move_count==0:
        return CONTINUE
    turn_x = not turn_x
    return CONTINUE
