def game_status():
    for i in range(0,3):
        if board[0][i]==board[1][i]==board[2][i]:
            if board[0][i]=="X":
                return WIN_X
            else:
                return WIN_0
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]:
            if board[i][0]=="X":
                return WIN_X
            else:
                return WIN_0
    if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        if board[1][1]=="X":
            return WIN_X
        else:
            return WIN_0
    k=0
    for i in range(3):
        for j in range(3):
            if type(board[i][j])!=int:
                k+=1
            if k==9:
                return DRAW
    return CONTINUE
def new_game():
    global board
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("поле обновленно")
    show_board()
    global turn_x
    turn_x=True
    return ""
def game_step():
    try:
        global turn_x
        if turn_x:
            print("ведите ,пожалуйста координаты 'X':")
        else:
            print("ведите ,пожалуйста координаты '0':")
        nuber= int(input())

        if nuber<4:
            y=board[0].index(nuber)
            x=0
        elif nuber<7:
            y=board[1].index(nuber)
            x=1
        else:
            y = board[2].index(nuber)
            x = 2
        if turn_x:
            if board[x][y]!="X" and board[x][y]!="0":
                board[x][y] = "X"
                turn_x = not turn_x
            else:
                print("координаты уже используються")
        else:
            if board[x][y] != "X" and board[x][y] != "0":
                board[x][y] = "0"
                turn_x = not turn_x
            else:
                print("координаты уже используються")
    except ValueError:
        print("Ведины не правельные координаты или до этого были использованы.")
    except IndexError:
        print("Ведины не правельные координаты zили до этого были использованы.")

def show_board():
    for el in board:
        print(*el)

CONTINUE=0
WIN_X=1
WIN_0=2
DRAW=3
board=[[1,2,3],[4,5,6],[7,8,9]]
score_x=0
score_0=0
show_board()
turn_x=True       #если флажок turn_x=False в масив добавляем "0" на указанные координаты если turn_x=True добовляем "X"
while game_status()==CONTINUE:
    game_step()
    show_board()
    if game_status()==WIN_X:
        score_x+=1
        print("ПОБЕДА КРЕСТИКОВ, крестики победили:",score_x,"нолики:",score_0,". что бы продолжить ведите 'next',закончить 'break'")

    elif game_status()==WIN_0:
        score_0+=1
        print("ПОБЕДА НОЛИКОВ, крестики победили:",score_x,",нолики:",score_0," что бы продолжить ведите 'next',закончить 'break'")


    elif game_status()==DRAW:
        print("НИЧЬЯ, крестики победили:",score_x,",нолики:",score_0,". что бы продолжить ведите 'next',закончить 'break'")

    if game_status()!=CONTINUE:
        while True:
            status = input()
            if status == "next":
                new_game()
                break
            elif status == "break":
                break
            else:
                print("вы вели не правельное значение")