#Le eccezioni sono situazioni anomale che si verificano durante l’esecuzione del codice.
#Python offre un meccanismo di gestione delle eccezioni per affrontare questi scenari e garantire che il programma non si interrompa in modo imprevisto.
#utilizzando le istruzioni try, except, else, finally

#L’istruzione try permette di inserire il codice che potrebbe causare un’eccezione. L’istruzione except viene utilizzata per gestire l’eccezione specifica che potrebbe essere generata.

try:
    valore = int(input("Inserisci un numero intero: "))
except ValueError:
    print("Errore: Inserisci un numero valido.")

#in questo specifico caso stiamo gestendo la possibilità che l'utente inserista un valore o una stringa in input che non sia un intero restituendo con l'except un messaggio di erroe personalizzato
#else invece in un try viene eseguita solo se nessuna eccezione è stata generata.
try:
    risultato = 10 / 2
except ZeroDivisionError:
    print("Errore: Divisione per zero.")
else:
    print("Il risultato è:", risultato)

#in questo caso tiamo gestendo la possibilità che il divisore sia uguale a 0, in quel caso restituiremmo l'errore che troviamo in except
#mentre se non ci saranno errori entreremo nell'else esponendo il risultato della divisione

#Per quanto riguarda il finally in un try invece viene sempre eseguita, indipendentemente se è stata generata un’eccezione o meno

try:
    file = open("file.txt", "r")
    contenuto = file.read()
except FileNotFoundError:
    print("Errore: File non trovato.")
#finally:
    #file.close()

#in questo caso indipendentemente dall'esito del try che dia errore o meno, il finally comporterà in tutti i casi la chiusura del file che stiamo in questo caso leggendo.
