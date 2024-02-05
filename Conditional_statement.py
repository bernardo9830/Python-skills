### if, else
#Le condizioni di controllo sono importanti per far eseguire al nostro programma delle operazioni in base alla casistica in cui ci troviamo
#Esempio
x=10
if x%2==0:
    print('Il numero è pari ')
else:
    print('il numero è dispari')
## L'else entra in gioco solamente se la condizione nell'if non è verificata


############
# shortand: la shortand si utilizza solamente se lo statament dopo l'if è uno solo:
if x%2==0: print('il numero è pari')
else:print('il numero è dispari')

######## A volte ci sono da verificare diverse condizioni ed in base alla condizione soddisfatta eseguiamo il codice. Ci entra in aiuto elif:
x=75
if 0<x<50:
    print('è un numero positivo minore di 50')
elif 50<=x<90:
    print('è un numero maggiore uguale di 50 e minore di 90')
else:
    print('è un numero maggiore di 90')
### if annestati
if x%2==0:
    print(x,' è pari')
    if x<10:
        print(x,' è pari e minore di 10')
else:
    print(x,' è dispari')

### Possiamo avere tanti if innestati quanto ne vogliamo a sfavore però della leggibilità del codice.


