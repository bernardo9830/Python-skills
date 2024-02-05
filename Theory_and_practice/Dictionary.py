#                                                        Dictionary


#BASCIC DICTIONARY

#Un dizionario è una struttura dati rappresentato da coppie chiave:valore. Immagina di voler salvare valori relativi ad elementi diversi
#i dizionari ci vengono in aiuto.
# RAPPRESENTIAMO IL SEGUENTE LISTINO PREZZI

# CAPUCCINO = 4.0EUR
# CAFFE' = 2.0EUR
# SPREMUTA = 5.0EUR
# CORNETTO = 2.0EUR

#creiamo il nostro dizionario prices
prices = {'cappuccino':8.0, 'caffè':2.0, 'spremuta':5.0, 'cornetto':2.0}   # chiave:valore

# se ora vogliamo conoscere il prezzo di un elemento del dizionario prices quindi il valore di un determinato elemento
#riusciamo ad accedere tramite la chiave a cui fa riferimento

print(prices['cappuccino']) # output 8.0


# Costruttore dict

new_prices=dict(cappuccino=8.0, spremuta = 5.0, caffe = 2.0)
print(new_prices)


#NESTED DICT
new_prices = {1:prices, 2:new_prices }
print(new_prices)
#per accedere ai valori delle chiavi utilizziamo un doppio indice
print(new_prices[1]['cappuccino'])  # output 8.0

