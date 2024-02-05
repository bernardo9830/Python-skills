#                                               COMPARISON OPERATORS

#Lista di operatori di comparazione

# < strictly less than
# <= less than or equal
# > strictly greater than
# >= greater than or equal
# == equal
# != not equal
# is object identity
# is not negated object identity
# in membership
# not in negated membership.

#Un  operatore di comparazione effettua un confronto tra due operandi e ritorna un valore booleano


#Confronto tra interi:

n_1 = 5
n_2 = 6

print(n_1 >= 6)  #output: 'False'

#se vogliamo effettuare più confronti tra interi contemporaneamente abbiamo a disposizione due modi:
#1)
print(n_1 <= n_2 and n_2 <= 100)

#2
print(n_1 <= n_2 <= 100)  #n_2 viene valutato una sola volta

#siccome come valore si ottiene un booleano, si possono allora utilizzare gli operatori logici con più espressioni

# CHAINING COMPARISON

print(n_1 + n_2 >= 20 or n_1 == n_2)

#True and Expression return l'ultima espressione
print(n_1 == 5 and n_1*n_2)  # output 30
print(n_1*n_2 and n_1 < n_2)   # output True

#True or Expression return la prima espressione
print(n_1 < n_2 or n_1*n_2)  # output True
print(n_1*n_2 or n_1 < n_2)  # output  30

#False and expression return False
print(n_1 == n_2 and n_1*n_2) #return False

#False or expression return  espressione
print(n_1 == n_2 or n_1*n_2)  # output 30
print(n_1*n_2 or n_1 == n_2) # output 30

