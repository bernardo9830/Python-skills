#I moduli consentono di suddividere il codice in file separati, rendendo il codice più modulare, riutilizzabile e mantenibile
#Un modulo in Python è un file che contiene definizioni di funzioni, classi e variabili
#Definiamo un modulo che compierà una specifica azione in questo caso saluta().
def saluta(nome):
    print(str(nome) + " " + "ti sta salutando")

#Qui richiamo la funzione saluta che abbiamo scritto all'interno del modulo
saluta("Luca")

#----------------------------------------------------------------------------------------------------------------------
#                                      IMPORT MODULI,  DATETIME, MATH

#In python possiamo importare i moduli come datetime math per gestire date, orari e altro
#Il modulo datetime ti consente di acquisire la data corrente, creare date personalizzate, formattare date e orari e svolgere altre operazioni temporali
#Il modulo math estende le capacità delle operazioni aritmetiche di base e ti consente di eseguire calcoli matematici complessi.

#per prima cosa per poter utilizzare i metodi di datetime/math dobbiamo importarlo all'interno del codice e abbiamo due metodi per farlo:

#                                                     DATETIME

#import date datetime --> così importeremo tutti i suoi metodi, ma se dovessimo aver bisogno solo di un metodo in particolare:
#Esempio:
import datetime

data_corrente = datetime.datetime.now()
print("Data corrente:", data_corrente)
#Abbiamo importato il modulo datetime e con il metodo, datetime.now/datetime.date andiamo a visualizzare in console data e ora corrente.
#import date from datetime --> così importeremo solo il metodo "date" evitando di dover appesantire il codice
#Esempio:

from datetime import date

data_personalizzata = date(2023, 8, 15)
print("Data personalizzata:", data_personalizzata)

#in questo caso abbiamo importato solo il metodo date da datetime e l'abbiamo modulato.
#Abbiamo anche la possibilità di poter "formattare" l'output di datetime in modo da garantire una miglior leggibilità per il fruitore.

#                                                   MATH

#Prima di utilizzare le funzioni del modulo math, è necessario importarlo nel tuo codice:
import math

print(dir(math))
#utilizzando la funzione dir() del modulo math, visualizzeremo in console tutte le funzioni che il seguente modulo mette a disposizione.

#                                             PIP
# moduli del Python Package Index vengono installati da terminale, tramite un programma chiamato PIP.
#inserendo nel terminale il comando "--version" possiamo controllare se PIP è installato e di quale versione possiamo usufruire
#il comando "pip list" ci permette di controllare i package installati
#pr installare un nuovo pacchetto utilizzeremo "pip install 'nomedelpacchetto'"
#fatto ciò poi potremmo richiamare i vari moduli all'interno del codice con la funzione import precedentemente spiegata.




