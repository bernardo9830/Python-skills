#                                              FILES IN PYTHON

#La logica nel lavorare con i file in python è la seguente: apri il file con la funzione open(), fai quello che devi fare
# e poi è importante chiudere i dati

#La funzione open() deve avere all'interno il path del file che stiamo cercando di aprire. Ad esempio supponendo che il file di testo
#myfile.txt si trovi nella directory corrente dove sto lavorando avremo:

file = open('myfile.txt')

#Un file testo si può aprire in diverse modalità:

#Modalità lettura :
#Il file aperto può essere solo letto e non sono consentite modifiche
# file = open('myfile.txt', 'r')

#Modalità scrittura:
#In questo caso il testo sarà riscritto e qualsiasi scosa scriveremo andrà a sovrascrivere il nostro file
# file = open('myfile.txt', 'w')

#Modalità append:
# In questo caso il testo sarà aggiunto alla fine del file di testo

#Modalità binaria:
# file = open('myfile.txt', 'b')

#Modalità testo:
# file = open('myfile.txt', 't')

#A volte si possono utilizzare combinazioni di modalità di lettura di un file

#file = open('myfile.txt', 'bw') cioè ci voglio scrivere in binario

#Alcune combinazioni non sono consentite: Ad esempio non posso aprire il file sia in modalità testo che binario

# Un parametro che può essere specificato in open è il tipo di encoding utilizzato per codificare o decodificare il testo
#file = open('myfile.txt', encoding ='UTF-8')

#Importante per la sicurezza dei dati è chiudere il file una volta che ci abbiamo lavorato:
#un modo per far ciò è la funzione close:
file.close()


#                                                    READING FILES

#Ci sono diversi modi di leggere un file
#-file.read()   legge il file linea per linea

#-file.read(size)  specificando il parametro size stiamo stabilendo quanti bytes per linea vogliamo leggere

#-fiel.readlines() legge il file come una lista di stringhe

#- loop sul file.


file = open('myfile.txt', 'r')
print(file.read(3)) # CIA
print(file.read(4)) # O A
print(file.readline(3))  # CIA O A TUT

file.close()

file = open('myfile.txt')

print(file.readlines()) # output ['CIAO A TUTTI COME VA?']

file.close()


#                                                  WRITING FILES

# Il metodo write() su un file che non esiste crea un nuovo file, mentre se esiste sovrascrive il contenuto

file = open('myfile.txt', 'w', encoding= 'utf-8')
file.write('HELLO EVERYONE')
file.close()

file = open('myfile.txt', 'r')
print(file.read())

file.close()

names = ['bernardo\n', 'carlo\n', 'luca\n']
file = open('myfile.txt', 'w')
for name in names:
    file.writelines(name)
file.close()

file = open('myfile.txt', 'r')
print(file.read())
file.close()

#                                                 METODO APPEND

file = open('myfile.txt', 'a')
file.write('RACHELE\n')
file = open('myfile.txt', 'r')
print(file.read())
file.close()



