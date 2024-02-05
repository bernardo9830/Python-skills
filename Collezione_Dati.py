#Le liste i dizionari le tuple i set servono per collezzionare dati.
# Una collezione di dati è ben ordinata se ha un ordine ben definito e l'aggiunta di un elemento non cambia l'ordine della collezione di dati
#Indicizzato: significa che possiamo accedere ad un dato da una collezione tramite un indice.
#Una collezione di dati è modificabile se posso aggiungere rimuovere o cambiare elementi. Esempio:Liste
#Immutabili: non possiamo aggiungere o cambiare o rimuovere elementi.
#Permette duplicati: possiamo avere più elementi dello stesso valore


#DEFINIZIONI DEI VARI TIPI DI COLLEZIONI DI DATI:
#----Liste:
    #sono collezioni di dati ordinati,modificabili e permettono duplicati.
#---- Tuple:
      #sono collezioni di dati ordinati e immutabili. Permettono duplicati.

           ####################################
#----- Set:
       #sono non ordinati e non permettono duplicati e non modificabili
#----- Dictionary:
       #sono ordinati modificabili, non permettono duplicati.

#-------------------------------------------------------------------------------------------------------------------
#                                                     LISTE
x=['milano','roma','crotone']
print(type(x)) #L'output ci fornisce il tipo di questo dato
print(len(x)) #L'output ci fornisce la lunghezza della lista
# usando il costruttore list possiamo creare una lista come segue:
y=list(('a','b','c'))

#Accedere agli elementi di una lista
print(x[0]) #L'output sarà 'milano' perchè l'indice parte da 0!
print(x[-1])# L'output sarà 'crotone', ovvero con indice negativo accediamo a ritroso agli elementi di una lista
#RANGE
print(x[:2]) #L'output sarà ['a','b']



### METODI APPEND(), INSERT(), EXTEND()
x.append('Cosenza') #Si aggiunge alla fine della lista x il valore 'Cosenza'
x.extend(y)  #si aggiunge alla lista x tutti i valori della lista y.
x.insert(0,'Reggio Calabria') #il primo valore della funzione indica l'indice(la posizione) dove vogliamo inserire 'Reggio Calabria'.


### Metodi di rimozione #remove() pop() del
x.remove('Reggio Calabria') #Eliminiamo il valore 'Reggio Calabria' dalla lista x
x.pop(0) #Elimina il primo elemento.
del x[1] #Si può eliminare un elemento o tutta la lista
y.clear() #La lista viene pulita e rimane una lista vuota


#-----------------------------------------------------------------------------------------------------------------------
#                                                          TUPLE
#Le tuple sono collezioni di dati ordinati non modificabili e non permettono duplicati
x=('milano', 'cosenza')
print(x)
y=tuple(('milano','torino','crotone'))
#la funzione len e type sono come quelle delle liste.
#Il modo di accedere ad una tupla è lo stesso delle liste

#siccome le tuple sono immutabili questa operazione x[0]=1 mi manderà a schermo un errore.
#x=(x)
#print(x)
#x[0]='crotone'


#unpack tuple se ci sono pù valori utilizziamo l'asetrisco vicino l'ultima variable
(m,n)=x
print(m,n)
# Il metodo count() ci permette di contare la ricorrenza di un valore nella tupla. Il metodo index ci da' l'indice della prima ricorrenza del valore specificato.
print(y.count('crotone'))
print(y.index('crotone'))

#-----------------------------------------------------------------------------------------------------------------------
#                                                            SET
#Collezione di dati non ordinati, non indicizzati, non modificabili e non permettono duplicati.
x={'milano','roma','napoli'}
#len type sono gli stessi metodi delle altre collezioni di dati. Il costruttore set() ha la stessa funzione degli altri costruttori
#siccome non sono indicizati allora dobbiamo accedere agli elementi tramite loop
for elem in x:
    print(elem)
# i metodi add(lavori su un nuovo insieme) e update(aggiorniamo l'insieme esistente) aggiungono rispettivamente un nuovo elementoe un nuovo insieme.
x.add('brindisi')
y={'Ischia','Vibo Valentia'}
x.update(y)
#i metodi remove() pop() clear() del() hanno la stessa funzione come nelle liste.
#Una differenza è tra discard() e remove(). Se vogliamo eliminare un elemento che non è nel set con remove() questo ci dà errore. Se invece lo facciamo con discard riotteniamo di nuovo lo stesso insieme
x.discard('bologna')
print(x)
# Differenza tra union() e update(). Entrambi servono per unire due set, ma union() crea un nuovo set mentre update solo l'aggiorna.
z=x.union(y) #sto facendo l'unione insiemistica tra x e y. Quindi gli elementi duplicati vengono presi solo una volta
#intersection()
z1=x.intersection(y) #prende gli elementi in comune
z3=x.symmetric_difference(y) #Prende quelli che sono contenuti in entrambi ed elimina i duplicati.




#-----------------------------------------------------------------------------------------------------------------------
#                                                           DICTIONARY
#I dizionari sono una coppia di dati chiave:valore ordinati, modificabili ma non permettono duplicati.
persona={'nome':'Bernardo', 'età':25, 'Data di nascita':'30/11/1998'}
persona['età'] #mi fornisce il valore associato alla chiave età
persona.get('nome') #mi fornisce il valore associato alla chiave
persona.keys() #mi fornisce una lista di chiavi
persona.values() #mi fornisce una lista di valori
print(persona.items()) #mi fornisce una liste di tuple e ciascuna tupla rappresenta una chiave e un valore
#Modificare e aggiungere elementi
persona['nome']='Carlo'
print(persona)
persona.update({'nome':'Anna'})
persona.pop('nome') #rimuove la chiave nome e il suo valore
#dictannidati:
persona2=persona.copy()
persona2.update({'indirizzo':{'Città':'Milano','Cap':'29392','Civico':3}})
print(persona2)
print(persona2['indirizzo']['Cap'])


