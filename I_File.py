#La gestione dei file è una parte essenziale della programmazione, poiché consente di interagire con i dati presistenti
#Python offre una varietà di operazioni per creare, modificare, leggere e scrivere file.
#Le operazioni che possiamo svolgere sui file sono le seguenti:

#“x”: Creazione. Crea un nuovo file, ma genera un errore se il file esiste già.

#“r”: Lettura (predefinita). Il file deve esistere.
#Esempio:
#file = open("nuovo_file.txt", "r") #qui apriamo il file 'nuovo_file.txt' e diamo il comando di lettura 'r'
#contenuto = file.read()
#file.close()
#print(contenuto)

#“w”: Scrittura. Crea un nuovo file o sovrascrive il file esistente.
#Esempio:
#file = open("nuovo_file.txt", "w")  #qui apriamo il file 'nuovo_file.txt' e diamo il comando di scrittura 'w'
#file.write("Contenuto del nuovo file.")
#file.close()

#“a”: Aggiunta (append). Aggiunge contenuti al file esistente.
#Esempio:
#file = open("file_da_aggiornare.txt", "a") #qui apriamo il file 'nuovo_file.txt' e diamo il comando di aggiunta 'a' che aggiungerà contenuti senza sovrascrivere
#file.write("Questo è un nuovo aggiornamento.")
#file.close()

