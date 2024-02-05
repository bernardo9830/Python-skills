#                                                    VARIABLES

#Possiamo vedere una variabile come una scatola dove ci mettiamo qualcosa perchè in un secondo momento vogliamo usare il contenuto di questa scatola.
#Una variabile permette quindi di salvare un tipo di dato all'interno per essere riusato nel nostro codice.
#Questa operazione si chiama assegnamento

#Assegnamento
month='NOVEMBER'  # il membro di destra è il valore di tipo stringa che stiamo assegnando alla variabile month.

# se quindi richiamiamo month ad esempio la mandiamo a schermo vedremo il suo contenuto
print(month)

#è buona pratica assegnare alle variabili un nome che rappresenti nella pratica cosa è quella variabile
#ci sono alcune regole da seguire per assegnare un nome alla variabile

#1)Non può iniziare con una cifra
#2) Deve iniziare con una lettera minuscola o maiuscola oppure con un underscore
#3) Non può iniziare con una parola chiave (int, def list etc..)


#Se utilizziamo una variabile che non abbiamo ancora definito all'interno del nostro codice otteniamo un errore

#print('day of week') #ERROR

# Possiamo assegnare ad una variabile già definita un altro valore che andrà a sovrascrivere il precedente assegnamento
month=12
print(month)
print(type(month))
#Questa possibilità di sovrascrivere l'assegnamento è chiamata dynamic typing
#Prestare attenzione a sovrausare il dynamic typing perchè in un codice troppo lungo dove abbiamo cambiato più volte il valore di una variabile
#potremmo avere problemi

#Possiamo anche assegnare ad una variabile un'altra variabile
a=10
b=a # in questo caso l'assegnamento va letto cosi: b fa riferimento all'assegnazione fatta su a quindi b=10
