
#Una classe è un prototipo di un oggetto nel mondo reale
#Si definisce oggetto l'istanza della classe prototipo.
#Andiamo ora a creare una classe Persona. Come sappiamo una persona ha degli attributi che la identificano: Nome, cognome, età.
#Inoltre una persona può compiere anche delle azioni quindi abbiamo nella nostra classe persona dei metodi adatti per la classe in questione.
class Persona:
    def __init__(self,nome,cognome): #Questo è il costruttore
        self.nome=nome
        self.cognome=cognome
    def saluta(self):
        print('ciao sono '+ self.nome)
#Andiamo ora a creare un istanza di questa classe(oggetto):
persona1=Persona('Bernardo', 'Valente')
persona2=Persona('Carlo', 'Giuliani')
persona1.saluta()
#Volendo accedere ad un attributo di un'istanza della classe:
print(persona1.nome)



##                                                  EREDITARIETA'
#L'ereditarietà è la proprietà per cui una classe riceve ed eredità tutte le proprietà e i metodi della sua  classe padre.

class Studente (Persona):
    def __init__(self, nome, cognome, classe):
        super().__init__(nome, cognome)
        self.classe=classe

    def saluta(self):
        print('Ti saluto dalla classe ' + self.classe)


Studente1 = Studente('Alfredo', 'Rossi', '5B')
Studente1.saluta()





