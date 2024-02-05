sequenza = input(
    'Inserite la sequenza di gioco, ESEMPIO: X0X_XX_OX ').upper()
lista_simboli = [sequenza[i:i + 3] for i in range(0, len(sequenza) - 1, 3)]
sequenza = sequenza.replace('_',' ')
print(sequenza)
lista_simboli = [sequenza[i:i + 3] for i in range(0, len(sequenza) - 1, 3)]
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
j, i = input('Inserisci due interi minori uguali a 3 ').split()
try:
    j = int(j)
    i = int(i)
    if 0 <= i <= 3 and 0 <= j <= 3:
        if lista_simboli[j][i] == 'X':
            print('Casella occupata')
        else:
            lista_simboli[j] = lista_simboli[j].replace(lista_simboli[j][i], 'X')
    else:
        print('DEVI INSERIRE INTERI VALIDI')
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
except ValueError:
    print(' VALUERROR: INSERISCI INTERI!!')
