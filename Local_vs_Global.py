#                                                      SCOPE


#Lo scope è la parte del programma dove una certa variabile può essere raggiunta dal suo nome

#Global vs Local variable

x = 2
def stampa():
    print(x)

stampa() # output 2 infatti stampa() non fa altro che mandare a schermo la variabile x che è stata definita
#fuori dalla definizione di funzione. Quindi x è una variabile globale e ci permette di comunicare con la funzione stampa()

# Le variabili globali sono utili per scambiare informazioni tra funzioni

#Local variable

def new_stampa():
    x = 3
    print(x)
# se chiamo new_stampa() ottengo 3 ma il valore della variabile x fuori dalla definizione di funzione new_stampa() è 2
new_stampa()
print(x)

def new_new_stampa():
    y = 'ciao a tutti'
    print(y)


#se chiamo y fuori lo scope ottengo un errore del tipo che non esiste nessuna variabile y. Questo perchè la variabile
# y viene raggiunta solo all'interno dello scope della function new_new_stamp()


#LEGB rule

#L'ordine con cui vengono raggiunte le variabili è il seguente:
#1)LOCAL
#2) ENCLOSING
#3) GLOBAL
#4) BUILT-IN

z = "global"
def outer():
    z = "outer local"
    def inner():
        z = "inner local"
        def func():
            z = "func local"
            print(z)
        func()
    inner()

outer()  # "func local"

#se da func() tolgo print(z) outer() mi restituisce a schermo inner local
def outer():
    z = "outer local"
    def inner():
        z = "inner local"
        def func():
            z = "func local"
            #print(z)
        func()
    inner()

outer() # 'inner local'

# se cancelliamo z all'interno di inner verrà stampato "outer local"

def outer():
    z = "outer local"
    def inner():
        #z='inner local'
        def func():
            #z = "func local"
            print(z)
        func()
    inner()
outer() # outer local


#keyword global and nolocal

#global

time = 10

# def incr_time():
#     print(time)
#     time = time +1   questo codice forniesc un errore perchè l'interprete cerca la variabile time nel local scope e cerca di risolverla

# se vogliamo utilizzare nella funzione una variabile che non è all'interno del local scope possiamo utilizzare
#la keyword global

def incr_time():
    global time
    print(time)
    time += 1

incr_time()

print(time)

incr_time() #possiamo notare come time intesa come variabile globale cambi
incr_time()
incr_time()

#nolocal
# con questa keyword assegniamo la variabile fuori dal local scope

def number():
    number = 10
    def inner():
        nonlocal number
        number = 5
        print('my favourite number is ', number)
    inner()
    print('outer variable number is ', number)


number() # il valore di number stampato in entrambi i casi sarà 5