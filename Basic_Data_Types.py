# Ogni data object (variabile o costante) ha un tipo (type). Il tipo rappresenta come può essere gestito questo oggetto,
# come salvarlo in memori, quali operazioni si possono effettuare con questo tipo di oggetto.



#                                                  STRINGS

#Ogni qualvolta abbiamo a che fare con dati e informazioni testuali stiamo maneggiando dei dati di tipo stringhe
#Le stringhe sono rappresentate da doppie virgolette o singole.
print("Hello world") #stampa una stringa
print(" ") # stampa una stringa vuota
print() # ha lo stesso risultato di print(" ")
print('Hello world') # ha lo stesso risultato della prima riga di codice

#                                                  NUMERICAL TYPES
# i tipi di dati numerici si distinguono in:
# int= sono i cosidetti numeri interi su cui possiamo fare le più svariate operazioni conosciute in matematica
# float= sono i numeri decimali importanti quando si lavora in ambito
print(5)  #intero
print(5.0) # float


#                                                PRINTING TYPES

#abbiamo una funzione che ci permette di scoprire il tipo di un dato
# questa è la funzione type.

print(type(5.0)) #output <class 'float'>
print(type(5))   # output <class 'int'>
print(type('5'))  #output <class str>


