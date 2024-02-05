#        Built-in Exceptions Types

#SYNTAX ERROR
#questo tipo di errore avviene durante la compilazione in byte-code in quanto sintatticamente il codice è sbagliato
#EXAMPLE
# i := 2

#TYPEERROR
#questo tipo di errore si manifesta quando il programma viene eseguito in quanto stiamo cercando di effetturare delle operazioni
#con dei tipi di dato per i quali quelle operazioni non sono definite

# a = 10
# b = 'ciao'
# sum = a + b  #TYPEERROR

#NAMEERROR
#Questo errore si manifesta quando cerchiamo di risolvere una variabile senza ancora definirla


#VALUEERROR

#In questo tipo di errore stiamo utilizzando il tipo di dato corretto ma lavoriamo con un valore di tipo sbagliato

#int('five')


#OSError è una classe di errori. in questa classe c'è anche FILENOTFOUNDERROR
# f = open('i_dont_exist.txt')
# # Traceback (most recent call last):
# #   File "main.py", line 1, in <module>
# #     f = open('i_dont_exist.txt')
# # FileNotFoundError: [Errno 2] No such file or directory: 'i_dont_exist.txt'



#Exception handling
#Se ad esempio lavoriamo con un programma che si interfaccia con un utente e quindi dobbiamo gestire dati presi da un utente
#è molto usuale incontrare degli errori che portano al crash del programma
#Possiamo gestire questi errori con la logica try-except

#TRY-EXCEPT CODE BLOCK

#-(try code block):  in questo blocco di codice si esegue il codice se non si incontrano errori


#-(except code block)  In questo blocco di codice si controlla se l'errore corrisponde con il tipo di eccezione
#che vogliamo gestire e si esegue il pezzo di codice all'interno.
#il code block all'interno dell'except viene eseguito solo se l'errore corrisponde con l'eccezione gestita altrimenti
#il programma va in crash perchè non sa come gestire questo errore


#-(else code block) per evitare di aumentare le righe di codice nel blocco di codice del try e quindi aumentare il rischio di un'altra eccezione
#utilizziamo un else il cui blocco di codice viene eseguito solo se non si incontrano eccezioni

# -(finally code block) La keyword finally ci permette di eseguire il codice dopo il try-except block code

a = int(input('inserisci un numero intero '))
b = int(input('inserisci un numero intero diverso da 0 '))
try:
    result = a / b
except ZeroDivisionError:
    print('ERROR: NON SI PUO\' DIVIDERE PER 0')
else:
    print( 'il risultato della divisione è ', result)
finally:
    print('programma eseguito')

#Molte volte non riusciamo a prevedere esattamente che tipo di eccezione bisogna gestire quindi in caso utilizziamo
# except EXCEPTION

# a = int(input('inserisci un numero intero '))
# b = int(input('inserisci un numero intero diverso da 0 '))
try:
    a = int(input('inserisci un numero intero '))
    b = int(input('inserisci un numero intero diverso da 0 '))
    result = a / b
except:
    print('ERROR: NON SI PUO\' DIVIDERE PER 0\n NON SI PUò INSERIRE UN TESTO')
else:
    print( 'il risultato della divisione è ', result)
finally:
    print('programma eseguito')