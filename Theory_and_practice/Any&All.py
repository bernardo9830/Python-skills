#                                                            ANY&ALL

#Le funzioni any and all prendono come argomento un oggetto iterabile e restituiscono TRUE o FALSE in base ad alcune valutazioni

#ANY

#questa funzione controlla se almeno un elemento dell'iterabile è TRUE
test = [1, 0, 0, 0]
print(any(test))

test_1 = [0,0,0]
print(any(test_1))

#Quindi ANY restituisce true se trova almeno un elemento che come booleano non sia false

#ALL
# immagginiamo di avere un test e superarlo solo se abbiamo risposto corretto a tutte le domande

test_2 = [1,1,1,1]
print(all(test_2))  # output True

test_3 = [0, 1, 1, 1]
#se sbagliamo pure una domanda il test non è passato
print(all(test_3))
