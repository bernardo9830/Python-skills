#ROCK-SCISSOR-PAPER is a well-known game, where we have only three options: win, lose, equal result.


# Write a program that reads input that states which option users have chosen.
# After this, your program must make users lose! That is, your program should always select an option that defeats the one picked by users.
# Once it finds this option, output the line Sorry, but the computer chose <option>, where <option> is the name of the option that the program's picked depending on the user's input.


# For example, if users enter rock, the program should print Sorry, but the computer chose paper and so on.

user_move = input('fai la tua mossa ')
move = ["scissor", "rock", "paper"]
if move[0] == user_move.lower():
    computer_move = move[1]
    print("Sorry, but the computer chose ", computer_move)
elif move[1] == user_move.lower():
    computer_move = move[2]
    print("Sorry, but the computer chose ", computer_move)
elif move[2] == user_move.lower():
    computer_move = move[0].lower()
    print("Sorry, but the computer chose ", computer_move)
else:
    print("Devi scegliere una mossa valida ")



