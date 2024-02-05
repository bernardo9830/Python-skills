# Description
# Tic-tac-toe is a game known all over the world. Each country may have its own version of the name, sometimes the rules are different, but the essence of the game remains the same. Below are the main rules that may be familiar to you since childhood.
#
# Tic-tac-toe is played by two players on a 3x3 grid. One of the players is 'X', and the other player is 'O'. X plays first, then O takes the next turn, and so on.
#
# The players write 'X' and 'O' on a 3x3 field.
#
# The first player that puts 3 X's or 3 O's in a straight line (including diagonals) wins the game.

# Objectives
# Your first task in this project is to print the game grid in the console output.
# Use what you've learned about the print() function to print three lines, each containing three characters (X's and O's) to represent a game of tic-tac-toe where all fields of the grid have been filled in.

print(' ______\n| X O X |\n| X O X |\n| O X O |\n ------')



# In this stage, you will write a program that:
#
# Reads a string of 9 symbols from the input and displays them to the user in a 3x3 grid.
# The grid can contain only X, O and _ symbols.
# Outputs a line of dashes --------- above and below the grid, adds a pipe | symbol to the beginning and end of each line of the grid,
# and adds a space between all characters in the grid.
import re
vittoria = False
while vittoria == False:
    diag_control = ''
    inv_diag_control = ''
    count = 0
    sequenza = input(
        'Inserite la sequenza di gioco, ESEMPIO: X0X_XX_OX ').upper()
    # gli underscore significano che ci sono ancora simboli da inserire
    # Controllo mosse invalide:
    pattern = r'^[_XO]+$'  # Pattern per corrispondere a stringhe composte solo da lettere
    stringa_da_controllare = sequenza
    match_result = re.match(pattern, stringa_da_controllare)
    if not match_result:
        print("Mosse invalide")
    conteggio_x = sequenza.count('XXX')
    conteggio_o = sequenza.count('OOO')
    if (conteggio_o == 1 and conteggio_x == 1) or conteggio_o > 1 or conteggio_x > 1 or len(sequenza) > 9 or abs(
            conteggio_x - conteggio_o) > 2:
        print('Mosse invalide')
        break
    lista_simboli = [sequenza[i:i + 3] for i in range(0, len(sequenza) - 1, 3)]
    print(lista_simboli)
    lista_simboli_spaced = []
    for j in range(3):
        spaced_symbol = ''
        for i in range(3):
            spaced_symbol += ' ' + lista_simboli[j][i]
        spaced_symbol += ' '

        lista_simboli_spaced.append(spaced_symbol)
    print(lista_simboli_spaced)
    print('  _______\n|{}|\n|{}|\n|{}|\n -------'.format(lista_simboli_spaced[0], lista_simboli_spaced[1],
                                                         lista_simboli_spaced[2]))
    for i in range(3):
        control_sequence = ''
        count += 1
        if vittoria == True:
            break
        for j in range(3):
            control_sequence += lista_simboli[j][i]
            if i == j:
                diag_control += lista_simboli[j][i]
            if  i == len(lista_simboli)-1-j:
                inv_diag_control += lista_simboli[j][i]
            if lista_simboli[j] == 'XXX' or control_sequence == 'XXX' or diag_control == 'XXX' or inv_diag_control=='XXX':
                print('X WIN')
                vittoria = True
                break
            elif lista_simboli_spaced[j] == 'OOO' or control_sequence == 'OOO' or diag_control == 'OOO' or inv_diag_control == 'OOO':
                vittoria = True
                print('O WIN')
                break
        if count == 3 and '_' not in sequenza:
            vittoria = True
            print('La partita finisce con un pareggio ')
            break















