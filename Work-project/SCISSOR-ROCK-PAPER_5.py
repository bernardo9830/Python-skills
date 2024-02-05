import random
name = input('Inserisci il nome ').title()
print(f'Hello {name}')
score = open('score', 'r')
details = score.readlines()
for i in range(len(details)):
    details[i] = details[i].replace('\n', '')
testo = ' '.join(details)
details = testo.split(' ')
score.close()
start = True
move = ["scissor", "rock", "paper"]
command = ['!exit', '!rating']
while start:
    user_move = input('fai la tua mossa ')
    if user_move == '!exit':
        start = False
        print('Bye')
        break
    if name not in details:
        details.append(name)
        details.append('0')
    if user_move == '!rating':
        if name not in details and len(details) < 2:
            details[0] = name
            details.append('0')
            print('Your score is 0')
        elif name in details:
            print(f'Your score is {details[details.index(name) + 1]}')
        else:
            details.append(name)
            details.append('0')
            print('Your score is 0')
        user_move = input('fai la tua mossa ')
        if user_move == '!exit':
            start = False
            print('Bye')
            break


    if user_move.lower() not in move and user_move.lower() not in command:
        print('Invalid input: mossa non valida')
    else:
        scores = int(details[details.index(name) + 1])
        index_move = random.randint(0,len(move)-1)
        computer_move = move[index_move]
        if computer_move == user_move.lower():
            print('IS A DRAW: COMPUTER CHOSE {}'.format(computer_move.upper()))
            details[details.index(name) + 1] = scores+50

        elif user_move.lower() == move[0]:
            if computer_move == move[1]:
                print('SORRY, COMPUTER HAS CHOSE {} SO YOU LOSE'.format(move[1].upper()))
            else:
                print('IT\'S FINE, COMPUTER HAS CHOOSE {}, SO YOU WIN'.format(move[2].upper()))
                details[details.index(name) + 1] = scores+100
        elif user_move.lower() == move[1]:
            if computer_move == move[0]:
                print('IT\'S FINE, COMPUTER HAS CHOOSE {}, SO YOU WIN'.format(move[0].upper()))
                details[details.index(name) + 1] = scores+100
            else:
                print('SORRY, COMPUTER CHOSE {}, SO YOU LOSE'.format(move[2].upper()))
        else:
            if computer_move == move[0]:
                print('SORRY, COMPUTER CHOSE {}, SO YOU LOSE'.format(move[0].upper()))
            else:
                print('IT\'S FINE, COMPUTER CHOSE {}, SO YOU WIN!'.format(move[1].upper()))
                details[details.index(name) + 1] = scores+100


score = open('score', 'w')
    # Itera attraverso la lista con passi di 2
for i in range(0, len(details), 2):
    score.write(f"{details[i]} {details[i + 1]}\n")
score.close()
