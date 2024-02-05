# Input()
#A volte abbiamo bisogno di interagire con l'utente. Quindi ricevere dati dall'utente e utilizzarli.
#La funzione di input() appena viene incontrata aspetta un valore inserito dall'utente

a = input()
print(a)

#è di buon uso chiarire che tipo di dato ci aspettiamo in input dall'utente. Questo si può fare in due modi:
#1) modo
nome = input('inserisci il tuo nome ')
età = input('inserisci la tua età ')
print('Ciao sono ' + nome + ' ho ' + età + ' anni')

#2) modo
print('inserisci il tuo nome')
name = input()
print('inserisci la tua età')
age = input()
print('Ciao sono ' + name + ' ho ' + age + ' anni')

#N.B ogni cosa inserita da input è una stringa.
print(type(input()))  # <class 'str'>



