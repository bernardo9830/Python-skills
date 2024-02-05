#                                             HTTP REQUEST & RESPONSE

#Un'HTTP request (richiesta HTTP) è un messaggio inviato da un client a un server secondo il protocollo HTTP.


#COMPONENTI HTTP REQUEST:

#Headers (Intestazioni):
#Contengono informazioni aggiuntive sulla richiesta, come il tipo di contenuto accettato dal client, l'encoding preferito, le informazioni sull'autenticazione, ecc.

#Body(Corpo):
#Presente solo nelle richieste che trasportano dati, come le richieste POST. Contiene i dati inviati al server.

#URL
#Specifica l'indirizzo della risorsa richiesta sul server.

#Metodo (Method):

#GET: Richiede la lettura di una risorsa.
#POST: Invia dati al server per essere elaborati (ad esempio, l'invio di dati di un modulo).
#PUT: Carica o aggiorna una risorsa sul server.
#DELETE: Elimina una risorsa sul server.



#Un'HTTP response (risposta HTTP) è un messaggio inviato da un server a un client in risposta a una richiesta HTTP ricevuta.

#STRUTTURA

#Status Line: contiene la versione di protocollo utilizzata, Uno status code, un numero a tre cifre che indica lo stato della richiesta

#Headers(intestazioni): Contengono informazioni aggiuntive sulla risposta, come il tipo di contenuto restituito, l'encoding utilizzato, informazioni sulla data di scadenza, ecc.

#Body (Corpo):

#Contiene i dati veri e propri inviati dal server al client. Questi dati possono essere di diversi tipi, come testo, HTML, JSON, immagini, ecc.


#Postman è un tool che ci permette di testare le varie API. Consete di effettuare request e visualizzare le respons. Inoltre possiamo fare il debug dei vari endpoint

#ESEMPIO(PROGETTO UNIVERSITY)


#HTTP REQUEST:POST http://localhost:5000/login

#Body: ruolo, matricola(o email_istituzionale dipende dalla selezione del ruolo), password

#Metodo= Stiamo facendo una richiesta POST cioè stiamo inviando i nostri dati per accedere


#HTTP RESPONSE:
# STATUS CODE 200 OK
# Body: in questa sezione su postman possiamo vedere il codice del messaggio ottenuto dalla response
# Headers: SERVER: Werkzeug/3.0.1 Python/3.12.0,  DATE: Fri, 24 Nov 2023 11:37:38 GMT, CONTENT-TYPE: text/html; charset=utf-8
#CONTENT LENGHT: 5435  SET-COOKIE: session=ec1caf1a-60a8-4fe8-9701-3ceb6002a1c0; Expires=Mon, 25 Dec 2023 11:37:38 GMT; HttpOnly; Path=/