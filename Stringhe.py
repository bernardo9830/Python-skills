#secondo corso:

#Castare significa prendere un valore di una stringa e convertirlo in un intero o float (e viceversa)
x='350'
print(type(x))
x=int(x)
y=x**2 #Questa operazione è possibile solamente perchè ho convertito la stringa in intero. Il casting quindi è necessario quando vogliamo effettuare delle operazioni che sono valide solo su un certo tipo di dato.
print(y)

#Stringhe
#il format: immagina di avere una stringa e vuoi concatenarla con un intero. Normalmente questa cosa non la puoi fare quindi usiamo questo metodo:
z=15
z1="ciao sono Luca e sono nato il {}"
print(z1.format(z))
#si può anche considerare di passare più valori al format in questo modo:
z1="ciao sono Luca e sono nato il {1}, ho {2} anni e peso {0}"
print(z1.format(70,z,26))

#slicing: Puoi accedere ai singoli caratteri di una stringa utilizzando l’indicizzazione e puoi estrarre sottostringhe utilizzando lo slicing.
stringa='Ciao a tutti'
print(stringa[0:4])
#Nel codice sopra ho printato la prima parola della stringa che parte da indice 0 fino a 4 non incluso.

#Metodi delle stringhe
#str.upper(): Restituisce una nuova stringa con tutti i caratteri in maiuscolo.
print(stringa.upper())
#str.lower(): Restituisce una nuova stringa con tutti i caratteri in minuscolo
print(stringa.lower())

