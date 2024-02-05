# Improve your program so that it will take an unlimited number of inputs until users enter !exit.
# After entering !exit, the program should print Bye! and terminate.
# Also, let's try to handle invalid inputs: your program should be ready to handle typos in user input, or when there's a mishmash instead of a normal command.
# So, if the input doesn't correspond to any known command (an option or !exit), your program should output the following line: Invalid input.

# Objectives
# Your program should:
#
# Take input from users;
# If the input contains !exit, output Bye! and stop the game;
# If the input is the name of the option, then pick a random option and output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
# Loss: Sorry, but the computer chose <option>
# Draw: There is a draw (<option>)
# Win: Well done. The computer chose <option> and failed
# If the input corresponds to anything else, output Invalid input;
# Repeat it all over again.

import random
start = True
move = ["scissor", "rock", "paper"]
while start:
    user_move = input('fai la tua mossa ')
    if user_move == '!exit':
        start = False
        print('Bye')
        break
    if user_move.lower() not in move:
        print('Invalid input: mossa non valida')
    else:
        index_move = random.randint(0,len(move)-1)
        computer_move = move[index_move]
        if computer_move == user_move.lower():
            print('IS A DRAW: COMPUTER CHOSE {}'.format(computer_move.upper()))
        elif user_move.lower() == move[0]:
            if computer_move == move[1]:
                print('SORRY, COMPUTER HAS CHOSE {} SO YOU LOSE'.format(move[1].upper()))
            else:
                print('IT\'S FINE, COMPUTER HAS CHOOSE {}, SO YOU WIN'.format(move[2].upper()))
        elif user_move.lower() == move[1]:
            if computer_move == move[0]:
                print('IT\'S FINE, COMPUTER HAS CHOOSE {}, SO YOU WIN'.format(move[0].upper()))
            else:
                print('SORRY, COMPUTER CHOSE {}, SO YOU LOSE'.format(move[2].upper()))
        else:
            if computer_move == move[0]:
                print('SORRY, COMPUTER CHOSE {}, SO YOU LOSE'.format(move[0].upper()))
            else:
                print('IT\'S FINE, COMPUTER CHOSE {}, SO YOU WIN!'.format(move[1].upper()))

