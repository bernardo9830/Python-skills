#                                                            IMPORT MODULES

#Un file contenente un elenco di operazioni che verranno lette e interpretate successivamente è chiamato script.
# Quando si scrivono programmi molto vasti ci potrebbe essere bisogno di utilizzare funzioni che abbiamo definito
#no nel nostro programma(perchè magari potrebbe complicare la leggibilità), o anche funzioni scritte da qualcun'altro
#Dobbiamo allora utilizzare dei moduli: L'utilizzo dei moduli ci permette di organizzare per bene il nostro codice

#I moduli sono file che contengono statements e definizioni. Hanno la .py exetension. Si caricano attraverso import

import math  #stiamo importando il modulo math tramite l'import statement

print(math.pi)  #math.pi ci permette di accedere alla variabile pi del modulo math
print(math.factorial(5))  #math.factorial() ci permette di accedere alla funzione factorial del modulo math

#A volte vogliamo importare dal modulo solamente alcune funzioni.

from math import factorial

x = factorial(3) #abbiamo importato solo la funzione factorial()

#E' buona pratica importare tutti i moduli all'inizio del codice.

#COSTRUZIONE MODULO

#per richiamare una funzione dal modulo c'è bisogno che sia stata definita all'interno della directory dove c'è il modulo

#wildcard import serve per importare tutti i nomi e le funzioni definite nel modulo
# from modulo import*


