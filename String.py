#                                                       STRING

#Le stringhe rappresentano un altro tipo di collezione di dati.
# A differenza delle liste però possono salvare solo caratteri.

#1) Le liste sono un tipo di dato immutabile. Questo significa che non puoi cambiare la stringa se prima non fai una copia di essa

saluto = 'ciao a tutti'

# saluto[0] = 'C'  fornisce un errore perchè la stringa saluto è immutabile

# Changing a string

# str.replace(old, new, count) replaces all occurrences of the old string with the new one. The count parameter is optional, and if specified, only the first count occurrences are replaced in the given string.
# str.upper() converts all characters of the string to upper case.
#
# str.lower() converts all characters of the string to lower case.
#
# str.title() converts the first character of each word to upper case.
#
# str.swapcase() converts upper case to lower case and vice versa.
#
# str.capitalize() changes the first character of the string to upper case and the rest to lower case.

#ESEMPI

print(saluto.replace('ciao', 'Hello'))
print(saluto.upper())
print(saluto.lower())
print(saluto.title())
print(saluto.swapcase())
print(saluto.capitalize())

#REMOVE CHARACTERS FROM A STRING

#I metodi per rimuovere caratteri da una stringa sono rstrip() lstrip() strip()

print(saluto.strip('ciao')) #rimuove il carattere dalla stringa
print(saluto.lstrip('c'))  #rimuove il carattere partendo da sinistra dalla stringa
print(saluto.rstrip('tutti')) #rimuove il carattere partendo da destra


#                           SPLITTING STRINGS AND JOIN LISTS

#possiamo passare da stringhe a liste e viceversa grazie ai metodi split e join.

#split()
print(saluto.split(" "))
#con split() prendiamo una stringa e passandogli un separatore decidiamo secondo quale criterio dividere la stringa e salvarla in una lista
#con l'esempio di prima abbiamo utilizzato come separatore lo spazio bianco

#il metodo split ha anche un altro parametro opzionale split(sep, maxsplit) maxsplit è un intero che ci dice
#quante volte utilizzare il separatore per dividere una stringa. La lista che otteniamo è di lunghezza maxsplit+1

print(saluto.split('a', 2)) # ['ci' , 'o ', ' tutti']

#il metodo split è utile anche per definire delle variabili con input dell'utente

nome, cognome = input('inserisci nome e congome ').split(' ')
print(nome)
print(cognome)

# Metodo join
# Il metodo join ci permette di ottenere da una lista una stringa con il vincolo che ogni elemento della lista deve essere una stringa

hello_list = ['ciao', 'a', 'tutti']

print(" ".join(hello_list))
print("_".join(hello_list))

#Typeerror int_list = [1, 2, 3]
# " ".join(int_list)  # TypeError!
saluti = 'ciao a\n tutti'
print(saluti)
print(saluti.splitlines())

#splitlines() permette di splittare prendendo come separatori le sequenze di escape
#splitlines contiene un parametro facoltativo che è keepends, questo è un valore booleano che se TRUE allora
# allora nello splitting le squenze di escape sono incluse
print(saluti.splitlines(keepends=True))
