#LE HTTP REQUEST sono le richieste inviate da un client al server

#Codici del tipo 1xx:
# Gli status code HTTP vengono utilizzati per indicare l'esito di una richiesta HTTP effettuata da un client a un server
#1xx (Informazioni): La richiesta è stata ricevuta, il server continua con il processo.

#100 Continue: Il client può continuare con la richiesta.
#101 Switching Protocols: Il server accetta di cambiare protocollo richiesto dal client.


#200(successo): La richiesta è stata ricevuta, compresa e accettata con successo.

#3xx (Redirezionamento): Ulteriori azioni devono essere intraprese al fine di completare la richiesta.


#4xx (Errore del cliente):

#400 Bad Request: La richiesta non può essere compresa o contiene sintassi errata.
#401 Unauthorized: Richiede l'autenticazione o la mancanza di autorizzazione.
#403 Forbidden: Il server ha capito la richiesta, ma rifiuta di eseguirla.
#404 Not Found: La risorsa richiesta non è stata trovata.

#5xx (Errore del server):  Il server ha fallito nell'eseguire una richiesta apparentemente valida.

#500 Internal Server Error: Il server ha riscontrato una situazione imprevista che impedisce il completamento della richiesta.
#503 Service Unavailable: Il server non è pronto a gestire la richiesta. Comunemente utilizzato quando è in manutenzione o sovraccarico.