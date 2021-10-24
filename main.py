game_board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"],
    ]
num = 0
player = "X"
print("Welcome to tic tac toe text based!!!")
# print(game_board)
while True:
    for board in game_board:
        print(board)
    if game_board[0][0] == player and game_board[0][1] == player and game_board[0][2] == player:
        print(f"{player} win!!")
        break
    elif "_" not in game_board[0] and "_" not in game_board[1] and "_" not in game_board[2]:
        print("draw")
        break
    elif game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        print(f"{player} win!!")
        break
    elif game_board[1][0] == player and game_board[1][1] == player and game_board[1][2] == player:
        print(f"{player} win!!")
        break
    elif game_board[2][0] == player and game_board[2][1] == player and game_board[2][2] == player:
        print(f"{player} win!!")
        break
    elif game_board[0][0] == player and game_board[1][0] == player and game_board[2][0] == player:
        print(f"{player} win!!")
        break
    elif game_board[0][3] == player and game_board[1][3] == player and game_board[2][3] == player:
        print(f"{player} win!!")
        break
    elif game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
        print(f"{player} win!!")
        break
    elif game_board[0][1] == player and game_board[1][1] == player and game_board[2][1] == player:
        print(f"{player} win!!")
        break
    for i in range(10):
        num += i
    if num == 1:
        player = "X"
    elif num % 2 == 0 :
        player = "O"
    elif num % 2 == 1:
        player = "X"
    try:
        fill = input('type a column and rows (1,1), h to see tutorial, x to exit the game\n').lower()
        if fill == "h":
            print("to fill the place you want, first you must type the row (we have three rows)\n \
                and you must type the column (we have three columns too) if you type (1,1)\
                it will fill in \n['x','_','_']\n['_','_','_']\n['_','_','_']\n")
        elif fill == "x":
            print('see you later....')
            break
        else:
            data = fill.split(',')
            game_board[int(data[0])-1][int(data[1])-1] = player
    except:
        print('sorry unknown value\n')
        continue
    

