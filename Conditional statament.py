#                                                           CONDITIONAL STATEMENT

#1) IF statement
#L'istruzione condizionale ha la seguenta struttura:
#if condition:
    #body of if statement

#Il codice all'interno dell'if viene eseguito solamente se la condizione è True

#ESEMPIO
price = int(input())
if price > 5000:
    print('Out of the budget')
print('Ok, i may buy it')

#IF NESTED
#ci possono essere più if e anche innestati:

acceptable_color = 'red yellow blue green orange'
rainbow_color = 'red orange yellow'
my_color = input('inserisci il tuo colore preferito ')
if my_color in acceptable_color:
    print("ok it's accetable color")
    if my_color in rainbow_color:
        print("it's a perfect color")
#il codice all'interno dell'if viene eseguito solo se la condizione è vera
#La condizione è un booleano o comunque un'espressione che restituisce un booleano

#                                               ELSE STATAMENT

#L'if-else  è un blocco di codice che viene eseguito in base alle condizioni che si verificano

# if condition:
#     print('Yes')
# else:
#     print('No')

#Il codice nell'else viene eseguito solo se la condizione nell'if è falsa.

if price > 100:
    new_price = price - price*30/100
else:
    print('no sconto')


#Shortcut:
print(new_price if price > 100 else 'no sconto' )



#ELIF STATAMENT

#L'elif serve per far eseguire un pezzo di codice se viene rispettata una condizione che nell'if invece non viene rispettata
#L'elif serve se le condizioni non sono mutuamente esclusive altrimenti mettendo due if consecutivi otteniamo un comportaento diverso

# basic elif syntax
# if condition1:
#     action1
# elif condition2:
#     action2
# else:
#     action3

#EXAMPLE

# elif example
price = 10000 # there should be some int value
if price > 5000:
    print("That's too expensive!")
elif price > 500:
    print("I can afford that!")
else:
    print("That's too cheap!")

#Se al codice di sopra mettiamo un altro if al posto dell'elif potrebbe sembrare che otteniamo lo stesso risultato.
#Ma non è cosi. Le due condizioni non sono mutuamente esclusive. Possiamo avere un prezzo che è maggiore di 5000 e quindi è anche maggiore di 500


price = 10000 # there should be some int value
if price > 5000:
    print("That's too expensive!")
if price > 500:
    print("I can afford that!")
else:
    print("That's too cheap!")

#QUESTO CODICE NON E' UGUALE A QUELLO DELL' ELIF-ELSE-IF

#se avessimo avuto delle condizioni mutuamente esclusive ad esempio
animale = 'cane'
if animale == 'cane':
    print('Io ho un ' + animale)
elif animale == 'gatto':
    print('io ho un ' + animale)
else:
    print('Non ho ne gatto, ne cane')

#in questo caso se al posto dell'elif sostituisco l'if la logica del codice è uguale perchè le condizioni sono mutuamente esclusive.
#una stringa non può essere contemporaneamente 'gatto' o 'cane'.


#EXERCISE
# Given the 3 sides of a triangle - x, y and z -
# determine whether the triangle is equilateral, isosceles or obtuse.
#                COSTRUZIONE TRIANGOLO
try:
    x = int(input('inserisci un numero positivo '))
    y = int(input('inserisci un numero positivo '))
    z = int(input('inserisci un numero positivo '))
    if x >= 0 and y >= 0 and z >= 0:
        a = x+y
        b = x+z
        c = z+y
        if z <= a and y <= b and x <= c:
            if x == y and x == z and z == y:
                print('Il triangolo è equilatero')
            elif x != y and z != x and y != z:
                print('il triangolo è scaleno')
            else:
                print('Il triangolo è isoscele')
        else:
            print('I numeri inseriti non soddisfano la disuguaglianza triangolare')
    else:
        print('ERROR: Hai inserito un numero negativo!!!')

except:
    print('ERROR: devi inserire un numero')




