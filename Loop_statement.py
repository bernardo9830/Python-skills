#Il while permette di creare un ciclo e le istruzioni dentro il while vengono eseguite fin quando la condizione del while è soddisfatta
### break continue ed els sono costrutti che vengono utilizzati dentro il while
i=0
while i<6:
    print(i)
    i+=1
# L'output di questo codice sono i numeri da 0 a 5.
#Se ad esempio volessimo fermarci quando incontriamo un numero dato:
j=0
while j<6:
    if j==3:
        break
    print(j)
    j+=1

#break ci serve per interrompere il codice:



#In questo codice stampiamo tutti i numeri naturali saltando il 3
k=0
while k<5:
    if k==3:
        continue
    print(k)
    k+=1


i=0
while i<2:
    print(i)
#Questo è un esempio di loop infinito.

#-----------------------------------------------------------------------------------------------------------------------
#                                                              FOR
#Il ciclo for lo usiamo per iterare su una sequenza di elementi, come una lista, una stringa o una sequenza numerica. Questa struttura di controllo consente di eseguire un blocco di codice per ogni elemento nella sequenza.
numeri=[1,2,3,4,5,6]
for numero in numeri:
    print(numero)
#Con questo ciclo stiamo leggendo tutti gli elementi della lista passata in argomento.

parola='Ciao'
for carattere in parola:
    print(carattere)
#In questo ciclo stiamo scomponendo la stringa parola in caratteri.

#Il ciclo for è ampiamente utilizzato quando è necessario eseguire un’azione per ogni elemento in una sequenza. Può essere utilizzato per elaborare liste, stringhe e sequenze numeriche.

numeri1=[1,2,3,4,5,6,7,8,9,10]
for numero1 in numeri1:
    if numero1%2==0:
        print(numero1)
#In questo ciclo stampiamo solo i numeri pari.

#Puoi annidare cicli for all’interno di altri cicli for o all’interno di strutture di controllo come le istruzioni if per gestire situazioni più complesse.
a=[[1,2,3,4],['a','b','c','d']]
for num in a:
    for elem in num:
        print(elem)
