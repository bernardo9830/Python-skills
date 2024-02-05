#                                            CREATING A MODULE

#Come abbiamo visto un modulo è un file di estensione .py salvato nella directory del progetto.
#I moduli vengono utilizzati principalmente quando si lavora con progetti di grandi dimensioni. Il principale punto
#a favore è la riusabilità del codice.
#Il modo per importare un modulo lo abbiamo già visto nel corso precedente:
#                                                            import module_name

#Uno script non è altro che un modulo che viene eseguito direttamente



#                                                Package

#Un package non è altro che una raccolta di moduli e subpackage. Ciascun package e subpackage contiente un file di estensione .py
# __init__.py che serve per specificare la il livello della directory.

#ESEMPIO

# package(Laptop)
#     - subpackage(Finance)
#           -crypto.py
#           -risk_analysis.py
#           -__init__.py
#     -Hell_word.py
#     -__init__.py

#Quando si lavora con progetti di grandi dimensioni è molto comodo per l'organizzazione dei file utilizzare i package



#Installazione di un package

#PIP :  pip è il package manager che installa tutti i package che sono nel Python Package Index(PyPI). Si può immaginare
# Python Package Index(PyPI) come una repository condivisa dove ci sono i vari pacchetti. Considera una libreria dove al posto dei libri
# ci sono i pacchetti e pip si "prende" un libro da questa libreria

# pip install name_package

# pip install numpy  # comando installazione della libreria numpy


#Import

#per importare questi pacchetti utilizziamo i seguenti comandi

# - import numpy  # importiamo il package numpy

# - import numpy as np # utilizziamo un alias per poi richiamare le varie funzioni np.array

# - from package_name import module_name # importiamo da un package un certo modulo

