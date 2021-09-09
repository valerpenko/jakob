def game_status():
    global board
    global move_count
    global turn_x
    player=X if turn_x else O
    winer=WIN_X if turn_x else WIN_O
    # проверям строки
    for i in range(0,3):
        if board[0][i]==board[1][i]==board[2][i]==player:
                return winer
    # проверям столбцы
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return winer
    # проверям ДИАГОНАЛИ
    if board[0][0]==board[1][1]==board[2][2]==player or board[0][2]==board[1][1]==board[2][0]==player:
        return winer


    if move_count==9:
        return DRAW
    if move_count==0:
        return CONTINUE
    turn_x = not turn_x
    return CONTINUE

def next_input():
    try:
        row, col = map(int, input("r,c:").split())
        return (row, col)
    except ValueError:
        pass

def game_step(row, col):
    global turn_x
    global board
    global move_count

    if board[row][col]!=EMPTY:
        return
    board[row][col]=X if turn_x else O
    move_count+=1



def show_board():
    global board
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                print("-",end='')
            elif board[i][j]==X:
                print("X", end='')
            elif board[i][j]==O:
                print("0", end='')
        print()

CONTINUE=0
WIN_X=1
WIN_O=2
DRAW=3
EMPTY=0
X=1
O=2
move_count=0
board=[[0 for i in range(3)] for i in range(3)]
turn_x=True #если флажок turn_x=False в масив добавляем "0" на указанные координаты если turn_x=True добовляем "X"
show_board()
while game_status()==CONTINUE:
    try:
        row,col=next_input()
        game_step(row, col)
    except ValueError:
        print("введите номер строки и номер столбца ")
    except TypeError:
        print("введите номер строки и номер столбца ")
    except IndexError:
        print("неверные координаты")
    show_board()

if game_status()==WIN_X:
    print("ПОБЕДА КРЕСТИКОВ")
elif game_status()==WIN_O:
    print("ПОБЕДА НОЛИКОВ")
elif game_status()==DRAW:
    print("НИЧЬЯ")