#                                                             LIST

# A volte abbiamo bisogno di raggruppare i dati. Le liste sono una collezione di dati

dog = ['pastore tedesco', 'carlino', 'barboncino', 'beagle', 'bassotto', 'alano', 'jack russel', 'husky']
print(dog)
#Il comando print(dog) ci stampa la collezione di dati salvata in dog proprio in quell'ordine proprio perchè le liste
#sono ordinate

#1) collezione di dati ordinate
#Siccome le liste sono ordinate possiamo accedere ai suoi elementi tramite indici
print(dog[0])  # manda a schermo il primo elemento
print(dog[-1])  # manda a schermo l'ultimo elemento

#SLICING
#Lo slicingo permette di ottenere una parte della lista la scrittura completa è la seguente:
#my_list[start:stop:step]
#start= indice da cui si parte a prendere l'elemento della lista
#stop= indice non incluso che indica l'ultimo elemento che sarà preso in my_list
#step= indica il passo con cui è effettuato lo slicing

#ESEMPI
print(dog[1:3])  # ['carlino', 'barboncino']=[dog[1],dog[2]]
print(dog[:])  # prende tutta la stringa
print(dog[1:7:2]) #parte da dog[1] e arriva a dog[6] prendendoli ogni 2 cioè l'output sarà ['carlino', 'beagle', 'alano']
print(dog[:5]) # parte di default
#SLICING NEGATIVO
print(dog[5:2:-1]) # si inizia a leggere la lista da destra a sinistra. Si parte dal dog[5] cioè 'alano' e all'incontrario si arriva fino
#a beagle

print(dog[2:7:-1]) # quando si usa lo slicing negativo l'indice di start deve essere più grande altrimenti si restituisce una stringa vuota

#REVERSE OF A STRING
#una stringa può essere vista come una lista
s = "wolf"
print(s[::-1])






#2) Oggetti iterabili
#le liste sono oggetti iterabili, cioè si possono prendere gli elementi della lista uno a uno
#La funzione list() ci permette di creare una lista
print(list('danger')) # otteniamo una lista delle lettere della parola danger splittate



#Le liste possono contenere qualsiasi tipo di dato, anche altre liste al suo interno

my_list = ['1', 2, ['1', 2, 'ciao', True]]

#MUTABILITA'

#Le liste sono mutabili cioè possiamo cambiare i propri valori
my_list[0] = 'ciao'
print(my_list)

#Le stringhe sono un esempio invece di collezione di dati immutabile
pet = 'dog'

#pet[0] = 'f' #in console leggiamo un errore che ci avvisa che l'oggetto str è immutabile non supporta l'assegnamento


#                                                   NESTED LISTS

#Come abbiamo visto nelle liste possono essere salvati qualsiasi tipo di dato, quindi possiamo salvare in una lista più liste
# Otteniamo quindi delle liste innestate

nested_list = ['1', 1, ['a', 'b', 'c']]
#per accedere agli elementi di una lista innestata possiamo usare il doppio indice
print(nested_list[2][2])  # output 'c' :  il primo indice è quello relativo alla posizione degli elementi nella lista 'madre', il secondo alla posizione degli elementi della lista figlia

#MATRICI
#un'ottima struttura dati sono le matrici.
#Le matrici sono liste di liste ecco un esempio:
diag_mat = [[1,0,0], [0,1,0], [0,0,1]] #matrice diagonale 3 x 3.

# Le liste rappresentano le righe della matrice

for i in range(3):
    for j in range(3):
        if i == j:
            print(diag_mat[i][j])             # output '1'. '1', '1' questo è un algoritmo per stampare gli elementi diagonale

#se invece voglio salvarli

diag = []
for i in range(3):
    for j in range(3):
        if i == j:
            print(diag_mat[i][j])
            diag.append(diag_mat[i][j])


# CREAZIONE MATRICE

#vogliamo creare la seguente matrice M = [[1,2,3],[4,5,6]]

matrix = []
for i in range(2):
    row = []
    if i == 0:
        for j in range(3):
            row.append(j+1)
        matrix.append(row)
    elif i ==1:
        for j in range(3):
            row.append(j+1)
        matrix.append((row))
print(matrix)

#Moltiplicazione matrice-vettore

v = [1,2,3]

mat = [[1,2,3], [0,0,1], [0,1,0]]

tot = []
for row in range(3):
    prod = 0
    for column in range(3):
        prod += mat[row][column] * v[column]
    tot.append(prod)
print(tot)    # [14, 3, 2]

#EXERCISE HYPERSKILL
#Let's say we have a matrix M:
#
# M = [[34, 77, 8,  45],
#      [10, 15, 93, 57],
#      [78, 82, 19, 98]]
# Write a code that will print the element in the first column and the third row. Mind that the size and the number of elements in the test matrix will be the same, but the integers in it will be different.



m = [[34, 77, 8,  45],
     [10, 15, 93, 57],
     [78, 82, 19, 98]]

dim_riga = len(m)
dim_col = len(m[0])

for riga in m:
    print(riga[0])   # stampo per ogni riga il primo elemento quindi ottengo la colonna [34,10,78]
for ind_column in range(dim_col):
    print(m[2][ind_column])    # fissata la terza riga scorro i suoi elementi






#LIST COMPREHENSION
# Questo è un metodo dove si utilizzano delle shortcut per scrivere liste in una sola riga di codice

cod = [i^2 for i in range(4)]  # output [0, 1, 4, 9]

# questo codice produce lo stesso risultato di questo:

cod_1 = []
for i in range(4):
    cod_1.append(i^2)

# con le shortcut la scrittura è più compatta

#Tuttavia abbiamo anche dei contro: Se lavoriamo ad un programma con molte righe di codice per un programmatore
#esterno potrebbe essere difficile interpretare

#Possiamo utilizzare questa scrittura anche con la costruzione di liste tramite condizioni di controllo
lista = [odd for odd in range(8) if odd % 2 == 0] # questa sarà un lista di numeri pari tra 0 e 7

# la struttura è cosi: partendo da sinistra dopo odd, il for è esterno e l'if è interno al for

lista_1 = [3*j + 1 for j in range(8) if j % 2 == 0 if j > 3]  # l'ultimo if è quello più interno

# possiamo introdurre anche l'else nell'if statement

# SINTASSI:

# [x if condition else y for x in some_iterable]

new_list = [num if num > 0 else 0 for num in [1,-2,3,-5,9,-2,0,-4,6] ]
print(new_list)
# otteniamo una lista dove al posto dei numeri negativi abbiamo lo zero
