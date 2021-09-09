import pygame
import sys
def game_status():
    player=X if turn_x else O
    winer=WIN_X if turn_x else WIN_O
    for i in range(0,3):
        if board[0][i]==board[1][i]==board[2][i]==player:
                return winer

    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return winer

    if board[0][0]==board[1][1]==board[2][2]==player or board[0][2]==board[1][1]==board[2][0]==player:
        return winer

    k=0
    for i in range(3):
        for j in range(3):
            if board[i][j]!=EMPTY:
                k+=1
    if k==9:
        return DRAW
    return CONTINUE
def game_step(row, col):
    try:
        global turn_x
        if board[row][col]!=EMPTY:
            return
        board[row][col]=X if turn_x else O
        turn_x = not turn_x
    except ValueError:
        pass
    except IndexError:
        pass
CONTINUE=0
WIN_X=1
WIN_0=2
DRAW=3
EMPTY=0
X=1
O=2
board=[[0]*3]*3
turn_x=True       #если флажок turn_x=False в масив добавляем "0" на указанные координаты если turn_x=True добовляем "X"



widht=height=80
margin=10
size=(widht*3+margin*4,widht*3+margin*4)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Крестики нолики")
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

while game_status()==CONTINUE:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type== pygame.MOUSEBUTTONDOWN:
            x_mouse ,y_mouse =pygame.mouse.get_pos()
            column=x_mouse//(margin+widht)
            row=y_mouse//(margin+height)
            game_step(row, column)
            # if board[row][column]!="0" and board[row][column]!="X":
            #     if turn_x:
            #         board[row][column]="0"
            #     else:
            #         board[row][column]="X"
            # turn_x=not turn_x
    for row in range(3):
        for col in range(3):
            if board[row][col]=="X":
                color=red
            elif board[row][col]=="0":
                color=green
            else:
                color=white

            x= col*widht+(col+1)*margin
            y = row * widht + (row+ 1) * margin
            pygame.draw.rect(screen,color,(x,y,widht,height))

    pygame.display.update()
if game_status()==WIN_X:
    print("ПОБЕДА ЗЕЛЁНЫХ")

elif game_status()==WIN_0:
    print("ПОБЕДА КРАСНЫХ")

elif game_status()==DRAW:
    print("НИЧЬЯ")