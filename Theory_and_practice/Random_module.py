#                                              Random Module

# Il modulo random ci permette di generare elementi tramite un algoritmo di cui il punto di partenza è seed
# Il seed controlla il comportamento della generazione di elementi
# La generazione non è totalmente randomica


#Importiamo il modulo


import random

print(random.random())  #random.random() produce un pseudo-random numero tra 0 e 1


#random.seed(5)  # specifichiamo un valore per il seed

print(random.random())

# Random basic functions
#-----------------------------------------------------------------------------------------

# random.uniform(a, b) produce un pseudo-float numero in un range(a, b) con distribuzione uniforme

print(random.uniform(5, 10))


#random.randint(a, b) ritorna un intero in un range(a,b) dove l'ultimo estremo è anche incluso

print(random.randint(3, 52))

#random.choice(seq)  # ci fornisce un elemento da una sequanza

print(random.choice('VOLDEMORT'))


#random.randrange(a, b, c)  #ritorna un numero in range(a, b) con step c

print(random.randrange(3, 100, 5))


#random.shuffle(seq) fa uno shuffle sugli elementi di una sequenza. E' necessario però che la sequenza sia un oggetto mutabile
x = [1,2,3,4,5,6]
random.shuffle(x)
print(x)

#random.sample(population, k) ritorna una sequenza di lunghezza k da una popolazione
print(random.sample(range(100), 3))

#random.gauss(mu, sigma) ritorna un valore  con distribuzione di probabilità gaussiana di parametri mu(media) e sigma(deviazione standard)
print(random.gauss(0, 1))  #normale standard

