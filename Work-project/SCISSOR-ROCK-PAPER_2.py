#This program is an update version of SCISSOR-ROCK-PAPER_1

#NEW OBJECTIVE
# Your program should:
#
# Read the user input that includes an option;
# Choose a random option;
# Compare the options and determine the winner;
# Output one of the lines above depending on the result of the game.

#new knowlodge: random module

import random
user_move = input('fai la tua mossa ')
move = ["scissor", "rock", "paper"]
if user_move.lower() not in move:
    print('Errore: mossa non valida')
else:
    index_move = random.randint(0,len(move)-1)
    computer_move = move[index_move]
    if computer_move == user_move.lower():
        print('IS A DRAW: COMPUTER CHOSE {}'.format(computer_move))
    elif user_move.lower() == move[0]:
        if computer_move == move[1]:
            print('SORRY, COMPUTER HAS CHOSE {} SO YOU LOSE'.format(move[1]))
        else:
            print('IT\'S FINE, COMPUTER HAS CHOOSE {}, SO YOU WIN'.format(move[2]))
    elif user_move.lower() == move[1]:
        if computer_move == move[0]:
            print('IT\'S FINE, COMPUTER HAS CHOOSE {}, SO YOU WIN'.format(move[0]))
        else:
            print('SORRY, COMPUTER CHOSE {}, SO YOU LOSE'.format(move[2]))
    else:
        if computer_move == move[0]:
            print('SORRY, COMPUTER CHOSE {}, SO YOU WIN'.format(move[0]))
        else:
            print('IT\'S FINE, COMPUTER CHOSE {}, SO YOU WIN!'.format(move[1]))




