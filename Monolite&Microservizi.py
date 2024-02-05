#Monolite: è un'applicazione costituita da una singola unità che contiene Database server application e client applicatione. Tutte queste parti del software sono impliementate e gestite in un solo posto.
#Nei microservizi un'applicazione è sviluppata dividendo l'applicazione in diversi servizi ciascuno dei quali gestisce una funzionalità diversa.
#Caratteristiche:



#Modularità:I servizi hanno lo scopo di suddividere in moduli l'applicazione.Ogni servizio espone un API per consentire ad un altro servizio l'utilizzo delle funzionalità implementate
#Queste Api sono un un confine invalicabili. Si violerebbe un principio fondamentale dei microservizi. Questa proprietà di disaccopiamento ci garantisce la scalabilità del servizio e la semplicità di rilascio. Per garantire un livello di disaccopiamento elevato è necessario che ogni servizio abbia un proprio database che non deve comunicare con un altro database.



#Indipendenza: Ogni servizio può essere sviluppato utilizzando tecnologie e linguaggi di programmazione diversi



#Scalabilità:I servizi possono essere scalati in modo indipendente in base al carico di lavoro specifico della funzionalità che gestiscono.Questo significa che si può gestire un aumento o una diminuizione del carico del lavoro ridistribuendo le risorse necessarie ai servizi
#Scalabilità tramite duplicazione dell'applicazione. Avere più istanze della stessa applicazione. Scalabilità sui dati, Scalabilità tramite separazione di funzionalità
#Scalabilità:La scalabilità permette di adattarsi dinamicamente al carico di lavoro in aumento o diminuzione.
# Puoi aggiungere o rimuovere risorse in modo flessibile in risposta alle esigenze del momento.
#Ad esempio, se un servizio di gestione utenti sta affrontando un aumento del carico, è possibile aumentare il numero di istanze di quel servizio senza influire sugli altri servizi.




#Isolamento degli errori: Nell'architettura monolite un errore porterebbe in crash l'intera apllicazione. Mentre nei microservizi un errore di un servizio non implica il malfunzionamento degli altri servizi



#Facilità di sviluppo e manutenzione:Gli aggiornamenti e le correzioni possono essere apportati a un singolo servizio senza influire sull'intero sistema.(Loose Coupling).



#High cohesion: I comportamenti correlati devono stare nello stesso posto. La modifica non deve avere problemi su altri servizi
