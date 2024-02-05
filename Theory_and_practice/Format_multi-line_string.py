#                                                                MULTI-LINE STRING

#A volte ci capita di scrivere delle stringhe molto lunghe e quindi è essenziale andare a capo. Perfare ciò
#ci sono alcuni metodi che possiamo utilizzare:
#1) TRIPLE QUOTES
print("""
HELLO
WORLD, THIS IS
MY FIRST
TASK 
 """)

#2) ESCAPE SEQUENCES
print("hello\nWORLD")

#\n è un escape charachter che non viene printato e manda a capo la stringa

# ----------------------------------------------------------------------------------------------------------------------
                                                    #FORMAT STRING

#vogliamo mandare a testo le nostre variabili con il valore a cui fanno riferimento direttamente nel testo. Il metodo
# meccanico che si può utilizzare è il seguente:

name = 'BERNARDO'
surname = 'VALENTE'
print('WELCOME ' + name + ' ' + surname)


#Tuttavia questo metodo può far apparire il nostro codice meno leggibile. Esaminiamo 3 modi di formattazione:


#1) USO DELL'OPERATORE  %
print('WELCOME %s %s' % (name, surname))
#tuttavia se abbiamo un testo abbastanza lungo questo modo di agire può intaccare la leggibilità del nostro codice

#2) USO DEL METODO str.format()
print('WELCOME {} {}'.format(name,surname))
#Le parentesi graffe sono dei placeholders e all'interno si passano le variabili name, surname nell'ordine in cui sono stati inseriti

#Volendo si può scegliere la posizione in cui voler stampare le due variabili
print('WELCOME {1} {0}'.format(name,surname)) # output WELCOME VALENTE BERNARDO

#OSS: se si passano più parametri nella funzione di quanti sono i placeholders il parametro in eccesso viene ignorato
#     se si passano più placeholders di quanti sono i parametri del metodo str.format() allora cadiamo in un INDEXERROR

print('WELCOME {name} {surname}'.format(name='Lionel',surname='Messi'))


#3) Uso della 'f' string
print(f'WELCOME {name} {surname}')
#questo è il metodo più veloce per far passare delle variabili in testo





#Ricapitolando
#i metodi principali sono 1 str.format(variable_1,variable_2....variable_n) e uso di placeholders nella stringa tanti quanto le variabili
#                          2 f'string' con placeholders contenenti direttamente le variabili