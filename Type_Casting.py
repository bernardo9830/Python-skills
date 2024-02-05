#                                               TYPE CASTING

#come sappiamo ogni variabile ha associato un tipo.
#Python è un linguaggio dynamic typed e strongly typed.

# dynamic typed vs static

#Essere un linguaggio dynamic typed significa che solo gli oggetti runtime hanno un tipo ma no le variabili dove salviamo i valori

v = 10

v = 'ciao'

#una volta eseguite le due righe di codice sopra il tipo di dato passa da intero a stringa. Questa proprietà è il dynamic typing


#Static typed language

#ci sono alcuni linguaggi però in cui le righe di codice di prima potrebbero dare errore. Questo perchè il tipo di dato deve essere
#dichiarato prima ancora di salvare il valore nella variabile
#Alcuni di questi linguaggi sono C, JAVA


# Strong vs. Weak typing
# strong typing significa che l'implicita conversione non avviene
# digits = '125'
# print(digits + 10) #TypeError digits non viene convertito automaticamente in numero

#L'operazione di convertire un tipo in un altro è chiamato casting
a = '125'
print(type(a))
a = int(a)  # abbiamo effettuato un casting
print(type(a))


