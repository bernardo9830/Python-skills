# The first player has to play as X and their opponent plays as O.
#
# Objectives
# In this stage, you should write a program that:
#
# Prints an empty grid at the beginning of the game.
# Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
# Ends the game when someone wins or there is a draw.
# You need to output the final result at the end of the game. Good luck!

# inserire le coordinate
# le coordinate inserite non esistono


#                                                       TIC TAC TOC

grid = []  #GRIGLIA
for riga in range(3):
    element = ''
    for column in range(3):
        element += ' '
    grid.append(element)

grid_spaced = [] # formattiamo la griglia per inserire spazi tra i simboli e mandarla a schermo in modo formattato
for j in range(3):
    spaced_symbol = ''
    for i in range(3):
        spaced_symbol += ' ' + grid[j][i]
        spaced_symbol += ' '
    grid_spaced.append(spaced_symbol)
print('   _0_1_2_\n0|{}|\n1|{}|\n2|{}|\n   -------'.format(grid_spaced[0], grid_spaced[1],
                                                         grid_spaced[2]))
count = 0
vittoria = False
while vittoria == False:
    count_o = grid[0].count('O') + grid[1].count('O') + grid[2].count('O')
    count_x = grid[0].count('X') + grid[1].count('X') + grid[2].count('X')
    if abs(count_x-count_o)> 1:
        print('GIOCO IMPOSSIBILE')
        break
    sequenza = input('Inserisci il simbolo X oppure O ').upper()
    if (sequenza != 'X' and sequenza != 'O'):
        if sequenza != 'exit' :
            print('Bye')
            break
        print('Non puoi inserire un altro simbolo: X o O')
        break
    if count % 2 == 0 and sequenza == 'O':
        sequenza = input('DEVI INSERIRE X ').upper()
    if count %2 == 1 and sequenza == 'X':
        sequenza = input('DEVI INSERIRE O ').upper()
    j, i = input('Inserisci le coordinate: ').split()

    try:
        j = int(j)
        i = int(i)
        if 0 <= i <= 3 and 0 <= j <= 3:
            if vittoria == True:

                break
            if grid[j][i] != ' ':
                print('Casella occupata')
            else:
                char = grid[j][i]
                char = grid[j][i].replace(char, sequenza)
                grid[j] =grid[j][0:i]+char.strip()+grid[j][i+1:len(grid[j])]
                print(grid)
                count += 1
                grid_spaced = []
                for j in range(3):
                    if vittoria == True:
                        break
                    spaced_symbol = ''
                    for i in range(3):
                        spaced_symbol += ' ' + grid[j][i]
                        spaced_symbol += ' '
                    grid_spaced.append(spaced_symbol)
                print('  ________\n|{}|\n|{}|\n|{}|\n --------'.format(grid_spaced[0], grid_spaced[1],
                                                                       grid_spaced[2]))
                for i in range(3):
                    control_sequence = ''
                    if vittoria == True:
                        break
                    for j in range(3):
                        control_sequence += grid[j][i]
                        if grid[j] == 'XXX' or control_sequence == 'XXX':
                            print('X WIN')
                            vittoria = True
                            break
                        elif grid[j] == 'OOO' or control_sequence == 'OOO' :
                            vittoria = True
                            print('O WIN')
                            break
                if grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X':
                    print('X HAI VINTO ')
                    vittoria = True
                    break
                if grid[0][0] == 'O' and grid[1][1] == 'O' and grid[2][2] == 'O':
                    print('O HAI VINTO ')
                    vittoria = True
                    break
                elif grid[0][2] == 'X' and grid[1][1] == 'X' and grid[2][0] == 'X':
                    print('X HAI VINTO ')
                    vittoria = True
                    break
                if grid[0][2] == 'O' and grid[1][1] == 'O' and grid[2][0] == 'O':
                    print('O HAI VINTO ')
                    vittoria = True
                    break
                elif count == 9 and vittoria == False:
                    print("La partita finisce in pareggio ")
                    break
                elif sequenza == '!exit':
                    print('Bye')
                    vittoria = False
                    break


        else:

            print('Le coordinate inserite non sono valide ')

    except ValueError:
        print('ERRORE: Le coordinate inserite non sono valite')