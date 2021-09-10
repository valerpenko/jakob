from x_o_core import *
#rgfd
def next_input():
    try:
        row, col = map(int, input("r,c:").split())
        return (row, col)
    except ValueError:
        pass

def show_board():
    global board
    for i in range(n):
        for j in range(n):
            if get_board(i,j)==EMPTY:
                print("-",end='')
            elif get_board(i,j)==X:
                print("X", end='')
            elif get_board(i,j)==O:
                print("0", end='')
        print()

n=int(input("укажите размер игровогополя: "))
init(n)
show_board()
row, col = next_input()
game_step(row, col)
show_board()
while game_status(row,col)==CONTINUE:
    try:
        row, col = next_input()
        game_step(row, col)
    except ValueError:
        print("введите номер строки и номер столбца ")
    except TypeError:
        print("введите номер строки и номер столбца ")
    except IndexError:
        print("неверные координаты")
    show_board()

if game_status(row,col)==WIN_X:
    print("ПОБЕДА КРЕСТИКОВ")
elif game_status(row,col)==WIN_O:
    print("ПОБЕДА НОЛИКОВ")
elif game_status(row,col)==DRAW:
    print("НИЧЬЯ")