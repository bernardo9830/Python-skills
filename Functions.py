#Le funzioni sono un blocco di codice riutilizzabili all'interno di un programma
#ci sono funzioni che non accettono argomenti e altre che accettono argomenti.
def prepara_lapasta(tipo_di_pasta):
    print("fai bollire l'acqua")
    print('metti la pasta:'+tipo_di_pasta)
#i parametri sono le variabili utilizzate nella definizione della funzione, gli argomenti sono i valori che passiamo alla funzione quando la chiamiamo
prepara_lapasta('spaghetti')

#A volte una funzione può accettare più di un parametro. Inoltre quando non sappiamo quanti parametri utilizzare si tratta di Key arbitrary arguments
def prepara_lapasta1(*opzioni):
    print("fai bollire l'acqua")
    print('metti la pasta '+opzioni[0])
    if opzioni[1]:
        print('metti il sugo')

prepara_lapasta1('spaghetti',True)

#Parametri di default
def prepara_lapasta2(tipo_dipasta = "spaghetti"):
    print("fai bollire l'acqua")
    print('metti la pasta:' + tipo_dipasta)
#Se non specifichiamo un argomento questa funzione quando viene chiamata utilizza come argomento spaghetti
prepara_lapasta2()

#Return valori utilizzando return abbiamo una funzione che produce qualcosa.
def somma(num1,num2):
    numtot=num1+num2
    return numtot


