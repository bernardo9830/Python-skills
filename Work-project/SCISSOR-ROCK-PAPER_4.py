# Objectives
# Your program should:
#
# Output a line Enter your name: . Users enter their names on the same line (not the one following the output!);
#
# Read input with the name and output a new line: Hello, <name>
#
# Read rating.txt and check whether it contains an entry with the current username. If yes, use the score specified in the file as a starting point. If not, start the score from 0.
#
# Play the game by the rules defined in the previous stages and read the user input;
#
# If the input is !exit, output Bye! and stop the game;
#
# If the input is the name of the option, then pick a random option and output a line with the result in the following format (<option> is the name of the option chosen by the program):
#
# Loss: Sorry, but the computer chose <option>
#
# Draw: There is a draw (<option>)
#
# Win: Well done. The computer chose <option> and failed
#
# For each draw, add 50 points to the score. For each win, add 100 points. In case a user loses, don't change the score;
#
# If the input corresponds to anything else, output Invalid input;
#
# Restart the game.


name = input('Inserisci il nome ').title()
print(f'Hello {name}')
score = open('score', 'r')
# for line in score:
#     print(line + '\n')
details = score.readlines()
for i in range(len(details)):
    details[i] = details[i].replace('\n', '')
testo = ' '.join(details)
details = testo.split(' ')

score.close()
x = '!rating'
score = open('score', 'a')
if x:
    if name not in details:
        print('Your score is 0')
        score.write(f'{name} 0')
    else:
        print(f'Your score is {details[details.index(name)+1]}')
score.close()



