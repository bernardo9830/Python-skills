#In Python così come anche in ltri linguaggi di programmazione, le variabili possono essere definite sia nell’ambito locale che in quello globale
#L’ambito di una variabile definisce dove è accessibile e modificabile.
#Esempio

#supponiamo di assegnare un valore ad una variabile e printarla in console

x = 1996
print(x)

#in questo caso stiamo richiamando un variabile che non è all'interno di una funzione ed è quindi facilmente richiamabile e modificabile all'interno del codice
#supponiamo invece poi di scrivere una funzione
def funzione ():
    y = 50
    print(x)
#in questo caso abbiamo una variabile locale che sarà riutilizzabile solo e soltanto all'interno della funzione a meno che non mettiamo un ritorno
#Esempio

#print(y)

#in questo caso siamo usciti dalla funzione e stiamo provando a richiamare una variabile locale, se facciamo partire il programma, esso ci restituirà un errore
#dicendoci che la variabile y non è stata definità poichè essa esiste solo all'interno della funzione che abbiamo definito sopra
#per ovviare al seguente problema abbiamo due escamotage che possiamo utilizzare
#la prima si può usare all'interno delle funzioni ed è la keyword "global" che consente di richiamre una variabile globale presente esternamente alla funzione
#l'altra è quella di inserire un ritorno della variabile di cui abbiamo bisogno alla fine della funzione che ci permetterà di richiamarla anche esternamente ad essa.
