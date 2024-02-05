#cosa sono i valori Booleani?
# I valori Booleani sono quei valori anche conosciuti come valori di verità. Vengono usati sopratutto per l'implementazione di condizioni di controllo come if else
#Valutazione dei valori booleani:
#   -bool(False), bool(0), bool(""), bool(()), bool([]),bool({}) restituiscono come valore sempre False.
x=0
if x:
    print('il telefono non si è ancora scaricato')
else:
    print('il telefono è scarico:',
          'bisogna metterlo a caricare')

#Questo perchè il valore di x è settato a 0 e un booleano che valuta zero restituisce False
