from random import seed, randint

BOARD_SIZE = 3
scene = "menu"
x = 0
y = 0

'''Starting function'''
def main():
    global scene
    if scene == "menu":
        drawMenu()
    
    pick = input(center_text("Input: "))
    while pick not in ['1', '2', '3', '4']:
        print(center_text(errorMsg()))
        pick = input(center_text("Input: "))

    options(pick)

'''Player vs computer game loop'''
def AI_game(player, AI, board, order, game_over, mode):
    turn = None
    if order == '1':
        turn = player
    elif order == '2':
        turn = AI
        
    isWinner = False
    row = ''
    col = ''

    while game_over == False:
        if turn == player:
            printLn()
            drawBoard(board)

            while isValidMove(board, row, col) != '':
                row = input("Enter row #: ")
                col = input("Enter column #: ")
                if isValidMove(board, row, col) != '':
                    print(isValidMove(board, row, col))
                    
            row = int(row)
            col = int(col)
            board = makeMove(board, turn, row-1, col-1)
        elif turn == AI and mode == '1':
            easyAI_Algorithm(board, turn)
        elif turn == AI and mode == '2':
            mediumAI_Algorithm(board, turn, player, game_over)
        elif turn == AI and mode == '3':
            hardAI_Algorithm(board, turn, player, game_over)

        game_over = isGameOver(board, turn, game_over,)[0]
        if game_over:
            game_over_screen(board, turn, game_over, mode, '', '', player, AI)
        if turn == AI:
            turn = player
        elif turn == player:
            turn = AI

        row == ''
        col = ''

'''Centers text passed in argument'''
def center_text(text):
    numOfSpaces = 0

    if len(text) % 2 == 1:
        numOfSpaces = 41 - int((len(text)-1)/2)
    elif len(text) % 2 == 0:
        numOfSpaces = 41 - int(len(text)/2)

    reAdjText = ''
    for i in range(0, numOfSpaces):
        reAdjText += ' '
        
    reAdjText += text
    return reAdjText

'''Draws 3 x 3 board for game'''
def drawBoard(board):
    global BOARD_SIZE
    displayArr = []
    tempArr = []
    char = ''
    displayLen = 3*BOARD_SIZE + 1 
    displayWidth = 5*BOARD_SIZE + BOARD_SIZE + 1

    # Creates board
    for i in range(0, displayLen):
        for j in range(0, displayWidth):
            if i == 0:
                if j == 0 or j == displayWidth-1:
                    char = ' '
                else:
                    char = '_'
            else:
                if j % 6 == 0:
                    char = '|'
                elif i % 3 == 0 and j % 6 != 0:
                    char = '_'
                elif (j-3) % 6 == 0 and (i-2) % 3 == 0:
                    global x
                    global y
                    if x == BOARD_SIZE:
                        x = 0
                        y += 1
                    char = board[y][x]
                    x += 1
                else:
                    char = ' '
            tempArr.append(char)
        displayArr.append(tempArr)
        tempArr = []
        char = ' '

    # Prints board
    for k in range(0, len(displayArr)):
        for m in range(0, len(displayArr[0])):
            print(displayArr[k][m], end="")
        print()
    print()
    
    x = 0
    y = 0

'''Draws main menu'''
def drawMenu():
    printLn()
    
    h_line = ''
    for i in range(0, 47):
        h_line += '#'
    print(center_text(h_line))
    
    
    print(center_text("# █████ ███ ███  ████████ ███  █████ ███ ████ #"))
    print(center_text("#   █    █  █      █  █ █ █      █   █ █ █    #"))
    print(center_text("  #   █    █  █      █  ███ █      █   █ █ █■■■ #  "))
    print(center_text("  #   █   ███ ███    █  █ █ ███    █   ███ ████ # "))

    h_line = ''
    for i in range(0, 47):
        h_line += '#'
        
    print(center_text(h_line) + "\n")
    guide = "*Enter the order number of your desired menu option to select it"
    print(center_text("Player VS AI"))
    print(center_text("Player VS Player"))
    print(center_text("Rules"))
    print(center_text("Credits\n"))
    print(center_text(guide.upper()))

'''Easy mode algorithm'''
def easyAI_Algorithm(board, turn):
    # If middle spot is empty, put symbol there
    if board[1][1] == ' ':
        board[1][1] = turn

    else:
        # Look for empty spots
        avail_spots = []
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == ' ':
                    avail_spots.append([i, j])
                
        # Put piece in a random spot
        seed(randint(0, 100))
        if len(avail_spots) > 1:
            dice = avail_spots[randint(0, len(avail_spots)-1)]
        else:
            dice = avail_spots[0]

        board = makeMove(board, turn, dice[0], dice[1])

'''Returns an error message for invalid input'''
def errorMsg():
    return "ERROR: NOT A VALID OPTION"

'''Goes to game over screen'''
def game_over_screen(board, turn, game_over, mode, p1, p2, player, AI):
    isWinner = isGameOver(board, turn, game_over)[1]
    printLn()
    drawBoard(board)
    print("GAME OVER!")
            
    if turn == p1 and isWinner:
        print("The winner is player 1.")
    elif turn == p2 and isWinner:
        print("The winner is player 2.")
    elif turn == player and isWinner:
        print("The player won the game.")
    elif turn == AI and isWinner:
        print("The AI won the game.")
    elif isWinner == False:
        print("The game is a tie.")

    play_again = input("\nWould you like to play again?(y/n): ")
    # Invalid input check
    while play_again.lower() != 'y' and play_again.lower() != 'n':
        print(errorMsg())
        play_again = input("Would you like to play again?(y/n): ")

    play_again = play_again.lower()
    if play_again == 'y' and AI != '':
        options('1')
    elif play_again == 'y' and AI == '':
        options('2')
    elif play_again == 'n':
        global scene
        scene = "menu"
        main()

'''Goes back to main menu'''
def goBack(go_back):
    global scene
    print("Enter 'b' to go back")
    
    go_back = input(center_text("Input: "))
    while go_back != 'b':
        print(center_text(errorMsg()))
        go_back = input(center_text("Input: "))
        
    go_back = ''
    scene = "menu"

'''Goes to credits from main menu'''
def goToCredits():
    printLn()
    print(center_text("CREDITS:\n"))
    print("Anirudh Palakkal\n")
    go_back = ''
    goBack(go_back)

'''Goes to rules from main menu'''
def goToRules():
    printLn()
    print(center_text("RULES:\n"))
    print("1. One player is assigned to use the letter 'X' and the other player" 
          + " is assigned to use the letter 'O'.\n")
    print("2. The players take turns putting their assigned symbol into the gird" +
          " until one player gets a column, row or diagnol filled with their " +
          "symbol or there are no more available spaces left in the grid.\n")
    print("3. The first player to make three consecutive occurances of thier " +
          "symbol in the form of column, row or diagnol wins the game.\n")
    print("4. If neither player gets three consecutive occurances of their" +
          "symbol in the form of a column, row nor diagnol and the grid has " +
          "no more spaces available, then the game is a tie.\n")
    go_back = ''
    goBack(go_back)

'''Hard mode algorithm'''
def hardAI_Algorithm(board, turn, player, game_over):
    # Find empty spots
    avail_spots = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == ' ':
                avail_spots.append([i, j])

    winning_spots = []
    losing_spots = []
    for i in range(0, len(avail_spots)):
        board[avail_spots[i][0]][avail_spots[i][1]] = turn
        # Find winning spots
        if isGameOver(board, turn, game_over)[0] == True:
            winning_spots.append(avail_spots[i])
        board[avail_spots[i][0]][avail_spots[i][1]] = ' '
        # Find losing spots
        board[avail_spots[i][0]][avail_spots[i][1]] = player
        if isGameOver(board, player, game_over)[0] == True:
            losing_spots.append(avail_spots[i])
        board[avail_spots[i][0]][avail_spots[i][1]] = ' '

    # If the center is empty, put symbol there
    if board[1][1] == ' ':
        board[1][1] = turn

    # If there is a winning spot, put symbol there
    elif len(winning_spots) != 0:
        board[winning_spots[0][0]][winning_spots[0][1]] = turn

    # If you there is a losing spot, block the player
    elif len(losing_spots) != 0:
        board[losing_spots[0][0]][losing_spots[0][1]] = turn

    # If you cannot win or lose in the next move, find potential winning spots
    elif len(losing_spots) == 0 and len(winning_spots) == 0:
        pot_win_streaks = []
        pot_lose_streaks = []
        
        # Find potential winning streak coordinates
        for i in range(0, len(avail_spots)-1):
            for j in range(i+1, len(avail_spots)):
                board[avail_spots[i][0]][avail_spots[i][1]] = turn
                board[avail_spots[j][0]][avail_spots[j][1]] = turn
                if isGameOver(board, turn, game_over)[0]:
                    pot_win_streaks.append(avail_spots[i])
                    pot_win_streaks.append(avail_spots[j])
                board[avail_spots[i][0]][avail_spots[i][1]] = ' '
                board[avail_spots[j][0]][avail_spots[j][1]] = ' '

        # Find potential losing streak coordinates
        for i in range(0, len(avail_spots)-1):
            for j in range(i+1, len(avail_spots)):
                board[avail_spots[i][0]][avail_spots[i][1]] = player
                board[avail_spots[j][0]][avail_spots[j][1]] = player
                if isGameOver(board, player, game_over)[0]:
                    pot_lose_streaks.append(avail_spots[i])
                    pot_lose_streaks.append(avail_spots[j])
                board[avail_spots[i][0]][avail_spots[i][1]] = ' '
                board[avail_spots[j][0]][avail_spots[j][1]] = ' '

        # Find spots that simultaneously help AI win and also block the player
        best_spots = []
        for i in range(0, len(pot_win_streaks)):
            for j in range(0, len(pot_lose_streaks)):
                if pot_win_streaks[i] == pot_lose_streaks[j]:
                    best_spots.append(pot_win_streaks[i])

        # If the spot blocks player and helps AI get a streak, put piece there
        if len(best_spots) != 0:
            seed(randint(0, 100))
            dice = best_spots[randint(0, len(best_spots)-1)]

        # If no such spot exists, put symbol on a potential winning streak spot
        elif len(best_spots) == 0 and len(pot_win_streaks) != 0:
            seed(randint(0, 100))
            dice = pot_win_streaks[randint(0, len(pot_win_streaks)-1)]
        
        # Else put symbol in a random spot
        elif len(best_spots) == 0 and len(pot_win_streaks) == 0:
            dice = avail_spots[0]
            
        board[dice[0]][dice[1]] = turn

'''Checks if game is over'''
def isGameOver(board, turn, game_over):
    isWinner = False
    count = 0

    # Checks for win
    for i in range(0, BOARD_SIZE):
        if (board[i][0] == turn and board[i][0] == board[i][1]
            and board[i][0] == board[i][2]):
            game_over = True
            isWinner = True
        if (board[0][i] == turn and board[0][i] == board[1][i]
            and  board[0][i] == board[2][i]):
            game_over = True
            isWinner = True
        if (board[0][0] == turn and board[0][0] == board[1][1]
            and board[0][0] == board[2][2]):
            game_over = True
            isWinner = True
        if (board[0][2] == turn and board[0][2] == board[1][1]
            and board[0][2] == board[2][0]):
            game_over = True
            isWinner = True

    # Checks for tie
    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE):
            if board[i][j] == 'X' or board[i][j] == 'O':
                count += 1

    if count == BOARD_SIZE**2 and isWinner == False:
        game_over = True
    return [game_over, isWinner]

'''Checks if player's coordinates are within board length'''
def isInRange(board, x, y):
    if (x < len(board) and x >= 0) and (y < len(board) and y >= 0):
        if board[x][y] == ' ':
            return True
        else:
            return False
    else:
        return False

def isValidMove(board, row, col):
    while (str(row).isdigit() == False or str(col).isdigit() == False
           or isInRange(board, int(row)-1, int(col)-1) == False):
        if str(row).isdigit() and str(col).isdigit() \
           and not(isInRange(board, int(row)-1, int(col)-1)):
                return "COORDINATES OUT OF RANGE"
        elif not(str(row).isdigit() and str(col).isdigit()):
            return "INVALID INPUT"
        else:
            return "SPOT ON BOARD ALREADY TAKEN"
    return ''

'''Puts player's symbol on board'''
def makeMove(board, turn, x, y):
    board[x][y] = turn
    return board

'''Medium mod algorithm'''
def mediumAI_Algorithm(board, turn, player, game_over):
    # Find empty spots
    avail_spots = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == ' ':
                avail_spots.append([i, j])

    winning_spots = []
    losing_spots = []
    for i in range(0, len(avail_spots)):
        board[avail_spots[i][0]][avail_spots[i][1]] = turn
        # Find winning spots
        if isGameOver(board, turn, game_over)[0] == True:
            winning_spots.append(avail_spots[i])
        board[avail_spots[i][0]][avail_spots[i][1]] = ' '
        # Find losing spots
        board[avail_spots[i][0]][avail_spots[i][1]] = player
        if isGameOver(board, player, game_over)[0] == True:
            losing_spots.append(avail_spots[i])
        board[avail_spots[i][0]][avail_spots[i][1]] = ' '

    # If the center is empty put symbol there
    if board[1][1] == ' ':
        board[1][1] = turn

    # If there is a winning spot, put symbol there
    elif len(winning_spots) != 0:
        board[winning_spots[0][0]][winning_spots[0][1]] = turn

    # If you there is a losing spot, block the player
    elif len(losing_spots) != 0:
        board[losing_spots[0][0]][losing_spots[0][1]] = turn

    else:
        # Look for empty spots
        avail_spots = []
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == ' ':
                    avail_spots.append([i, j])
                
        # Put piece in a random spot
        seed(randint(0, 100))
        if len(avail_spots) > 1:
            dice = avail_spots[randint(0, len(avail_spots)-1)]
        else:
            dice = avail_spots[0]

        board[dice[0]][dice[1]] = turn

'''Main menu options'''
def options(pick):
    global scene
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    if pick == '1': # If user picks player vs AI
        order = ''
        player = ''
        mode = ''
        AI = ''

        order = input("\nWould you like to go first or second? (1/2): ")
        while order != '1' and order != '2':
            print(errorMsg())
            order = input("Would you like to be player 1 or player 2 (1/2): ")
            
        print("\nWould you like to use X or O?")
        player = input("Type in your prefered symbol: ").upper()
        while player != 'X' and player != 'O':
            print(errorMsg())
            player = input("Type in your prefered symbol: ")
            player = player.upper()
            
        print("\nIn what mode would you like to play?")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        mode = input("Mode: ")
        while mode not in ['1', '2', '3']:
            print(errorMsg())
            mode = input("Mode: ")
            
        if player.upper() == 'X':
            player = 'X'
            AI = 'O'
        elif player.upper() == 'O':
            player = 'O'
            AI = 'X'

        scene = 'game'
        AI_game(player, AI, board, order, False, mode)
    elif pick == '2': # If user picks player vs player
        p1 = '1'
        p2 = '2'
        
        print("\nWould player 1 like to be X or O?")
        symbol = input("Type in your prefered symbol: ")
        symbol = symbol.upper()
        while symbol != 'X' and symbol != 'O':
            print(errorMsg())
            symbol = input("Symbol: ").upper()

        if symbol == 'X':
            p1 = 'X'
            p2 = 'O'
        elif symbol == 'O':
            p1 = 'O'
            p2 = 'X'

        scene = 'game'
        playerGame(p1, p2, board, False)
    elif pick == '3': # If user wants to see rules
        scene = 'rules'
        goToRules()
    elif pick == '4': # If user wants to see credits
        scene = 'credits'
        goToCredits()

'''Player vs player game loop'''
def playerGame(p1, p2, board, game_over):
    turn = p1
    row = ''
    col = ''
    
    while game_over == False:
        printLn()
        
        if turn == p1:
            print("It is Player 1's turn.")
        elif turn == p2:
            print("It is Player 2's turn.")
            
        drawBoard(board)
        
        # Invalid input check
        while isValidMove(board, row, col) != '':
            row = input("Enter row #: ")
            col = input("Enter column #: ")
            if isValidMove(board, row, col) != '':
                print(isValidMove(board, row, col))
             
        row = int(row)
        col = int(col)
        board = makeMove(board, turn, row-1, col-1)
        game_over = isGameOver(board, turn, game_over)[0]
    
        if game_over:
            game_over_screen(board, turn, game_over, '', p1, p2 ,'', '')
        else:
            if turn == p1:
                turn = p2
            elif turn == p2:
                turn = p1
        row = ''
        col = ''

'''Prints seperating line for new screen'''
def printLn():
    for i in range(0, 81):
        print("_", end="")
    print()

while scene == 'menu':
    main()
