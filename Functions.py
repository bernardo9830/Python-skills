#                                                       FUNCTIONS

#Le funzioni sono pezzi di codice riutilizzabili più volte nel nostro programma

#In python ci sono delle built-in function, cioè delle funzioni già definite che possiamo tranquillamente richiamare
#print() è un esempio di built-in function

print('hello world') #Questa funzione prende come argomento 'hello world' e lo manda a schermo

#print è una funzione che può anche non prendere nulla come argomento. Inoltre è una funzione che non restituisce nulla

a = print ( 'hello world' )

print(type(a))  #NONETYPE

#A volte ci serve scrivere delle funzioni di conto proprio per utilizzarle nel nostro programma e renderlo più efficiente e leggibile

#                                                        DEFINIZIONE DI FUNZIONE

#per costruire una funzione usiamo la keyword def (define)
#def verrà seguito dal nome della funzione che deve essere in minuscolo e contenere un underscore per separare due parole
# dopo il nome della funzione si aprono due parentesi tonde dove inseriremo i parametri(se accetta parametri) che servono alla funzione che utilizzerà nel blocco di codice
#dopo i due punti si ha un'identazione di 4 spazi per scrivere il blocco di codice della nostra funzione
# Se vogliamo che la nostra funzione restituisca qualcosa dobbiamo utilizzare la keyword return

#EXAMPLE OF FUNCTION'S BODY

def saluto(name):
    print('ciao ' + name)   # questo è il blocco di codice del corpo della funzione
    return name


#Invocazione della funzione

#per richiamare la funzione dobbiamo passargli un argomento o più argomenti dipende dalla definizione della funzione in base a quanti
#parametri utilizza

#Nel caso di saluto() questa richiede un solo argomento

saluto('BERNARDO') #output ciao bernardo  e osserviamo che la funzione effettivamente ritorna qualcosa

#Il valore che ritorna la funzione si può salvare in una variabile e riutilizzarlo. Ecco quindi l'efficienza delle funzioni

nome = saluto('BERNARDO')
print(nome)  #BERNARDO

#alla funzione saluto possiamo passare anche un argomento diverso da BERNARDO, questa è chiamata riutilizzabilità delle funzioni

#                                                                   PARAMETRI E ARGOMENTI

#c'è una differenza tra parametri e argomenti. Consideriamo questa funzione:
def ready(temp):
    if temp > 0:
        pass
    return 'SIAMO PRONTI!!'

#La funzione ready accetta un parametro temp, il parametro può essere visto come un alias dove verranno salvati i valori specifici che diamo in argomento alla funzione
#quando richiamiamo la funzione abbiamo bisogno di passargli un valore: quello è detto argomento e finira salvato nel parametro temp
go_on = ready(0) #0 è l'argomento
print(go_on)

#Una funzione può accettare più parametri per esempio:
def somma_modulo(num1, num2, num3):
    num_modulo = (num1 +num2 + num3) % 3
    return num_modulo

#La funzione somma_modulo prende tre parametri e calcola a loro somma in modulo 3

print(somma_modulo(10, 15, 2)) #output = 0

#10, 15, 2 sono gli argomenti

#SE PROVIAMO A PASSARE PIU' ARGOMENTI O MENO DI QUANTI NE ACCETTA LA FUNZIONE OTTENIAMO UN ERRORE

#somma_modulo(1)  #TypeError: somma_modulo() missing 2 required positional arguments: 'num2' and 'num3




#help()
#Per capire la struttura di una funzione o cosa fa possiamo utilizzare help()

help(len)
