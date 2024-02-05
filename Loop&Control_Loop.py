#                                               FOR LOOP


# I loop sono una ripetizione di codice più volte. I loop sono utili a svolgere compiti che per l'essere umano
#possono essere ripetitivi e noiosi e lo fanno senza errori.

#Ci sono due tipi di loop:
#1) I loop con numero di iterazioni definito
#2) I loop con numero di iterazioni non definito


# for variable in iterable_object:
#          statement

#il codice viene ripetuto per quanti elementi contiene l'oggetto iterabile

#ESEMPIO

#la stringa è un oggetto iterabile quindi possiamo fare lo spelling con il for:

for lettera in 'Maoiri':
    print(lettera)

# utilizzo di range()

for num in range(5, 50, 5):
    print(num)
# stampiamo i numeri da 5 a 50 con un passo di 5

#NESTED FOR
#ci possono essere for innestati:

for name in ['ROSA', 'MARIA']:
    for surname in ['MILLER', 'HEISENBERG']:
        print(name, surname)

#EXERCISE

# Assigning specific messages to numbers in a list
# You have a list of integers from 1 to 5 and you need to output each of the numbers in this list,
# along with a corresponding message based on each number's value.
# The message is 'is greater than 3.' if the number is more than 3 and 'is not greater than 3.' for all other cases.

int_list = [num for num in range(1,6)]
for num in int_list:
    if num > 3:
        print('is greater than 3')
    else:
        print('is not greater than 3')

# OSS: SI POTEVA FARE CON UNA SHORTCUT
for num in int_list:
    print('is greater than 3') if num > 3 else print('is not greater than 3')



# WHILE LOOP

#Come detto in precedenza esistono dei loop in cui non è fissato il numero di volte in cui si deve compiere il compito
#ma viene eseguito fin quando viene soddisfatta una certa condizione
#Per implementare questa logica di codice utilizziamo il WHILE LOOP


#SINTASSI:
# dopo la keyword abbiamo la condition code che è la condizione che deve essere soddisfatta
#per eseguire ciò che c'è all'interno del while, #che è chiamato block code
count = 0  # questa variabile gioca il ruolo di contatore, e ci permette di entrare nel while e valutare la condizione di controllo
while count < 5 :
    print(count)
    count += 1

# INFINITE LOOP

#I loop infiniti avvengono perchè la conditional code non è mai falsa cioè non avvengono cambiamenti

# ESEMPIO
# while True:
   #print('pending')

# A volte possono essere utili perchè vogliamo rimanere in attesa di risposta di un utente

#ESERCIZIO
#COUNT ITERATION
number = 0
while number < 12:
   print(number)
   number += 2

#L'output sarà il print di number STAMPATO PRIMA CHE VIENE AUMENTATO e ci saranno 6 iterazioni


# How many letters 'a' will be printed after this code is executed?

i = 0
a = 'a'
while i < 8:
    a *= 2
    i += 1
print(a)

#in questo codice ci sono 8 iterezioni e vengono stampate ben 2^8 'a' in generale sia n il numero di iterazioni
# in questo codice vengono stampate 2^n 'a'

#                                              CONTROL LOOP

#break: A volte voglia terminare un loop quando succede qualcosa. La keyword break ci permette di uscire dal loop e continuare
#nell'eseguire il blocco di codice successivo

#Vogliamo scorrere alcune parole salvate in una lista e terminare il loop se ne incontriamo una di lunghezza 3

parole = ['ciao', 'come', 'stai', 'Non', 'Bene']

for parola in parole:
    print(parola)
    if len(parola) == 3:
        print(parola, 'ha lunghezza 3')
        break
print('END')

#Continue : Il continue ci serve se in un loop vogliamo saltare un'operazione se accade qualcosa ma comunque vogliamo rimanere nel loop
# e skippare al passo successivo

for char in parole:
    if len(char) == 3:
        continue
    print(char)

# pass: Vogliamo tenere in considerazione qualcosa ma non eseguire nulla

for num in [1,2,3,4,5]:
    if num > 4:
        pass

