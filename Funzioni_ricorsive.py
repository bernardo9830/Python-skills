#                                                  Funzioni ricorsive

#Cosa è una funzione ricorsiva: Una funzione ricorsiva è una funzione che richiama se stessa per un numero finito di volte.
#La funzione ricorsiva è formata cosi: procedura di controllo(detto anche stato base o condizione di uscita,perchè il codice deve essere eseguito un numero finito di volte) e chiamata della funzione stessa con parametro argomento che cambia.


#somma dei primi n numeri
def somma(n):
    risultato=n
    if n!=0:           #Questa è la mia condizione di controllo. Continua a chiamare somma() fin quando n è diverso da 0
        n=n-1          #Chiaramente devo scalare di un un unità se voglio fare la somma dei primi n numeri interi partendo da n e andando all'indietro
        risultato+=somma(n)   #Richiamo la funzione
    return risultato
print(somma(5))



#Un altro esempio può essere il seguente: La funzione fattoriale può essere definita come una funzione ricorsiva:
def fattoriale(n):
    risultato=n
    if n==0:
        return 1
    else:
        risultato=risultato*fattoriale(n-1)
    return risultato

print(fattoriale(5)) #Ci aspettiamo 5*4*3*2*1=120


#Un altro esempio pratico è il seguente: Immagina di avere una stringa dove ci sono un sacco di spazi bianchi e non sappiamo quanti! Vogliamo ottenere la lista ripulita.
chiave_seriale='1   2        4  5          8          9'
chiave=chiave_seriale.split(' ')
print(chiave)
#Un modo per ripulire la lista sarebbe contare quanti spazi bianchi ci sono e implementare un ciclo for che ci rimuove gli spazi bianchi.
#Il metodo che implementiamo noi è di ripulirlo con una ricorsione:
def pulizia(testo):
    if '' not in testo: return testo
    else:
        testo.remove('')
    return pulizia(testo)

print(pulizia(chiave))


#Inversione di una parola tramite la ricorsione:
def inverti(parola,x=''):
    if len(parola)==0:
        return x
    else:
        x+=parola[-1]
        parola=parola[0:len(parola)-1]
        return inverti(parola,x)
print(inverti('ciao'))


def inverti1(parola):
    if len(parola)==1: return parola
    return parola[-1]+inverti(parola[:-1])






