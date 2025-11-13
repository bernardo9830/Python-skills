#COSA SONE LE API
#Le API sono interfacce di programmazione che permettono lo scambio di informazioni tra micro-servizi di un applicativo.
# Le API definiscono i metodi e i formati dei dati che possono essere utilizzati per interagire con un'applicazione o un servizio.
#Le API semplificano il design e l’architettura dei software, aggiungono flessibilità e sicurezza e permettono scalabilità e manutenzione nel tempo.
# Esistono vari tipi di API, ciascuno con caratteristiche specifiche.
#
# In una API agiscono due attori:
#
# Server: ossia l’unità che su richiesta fornisce i dati rispondenti alla chiamata e implementa le regole di funzionamento dell’API.
# Client: l’utente che effettua la chiamata (API call) per ottenere in ritorno dei dati. Il Client non ha necessità di conoscere il funzionamento del programma sottostante il Server, ma solo delle regole necessarie per implementare la chiamata.

#Il dialogo tra client e server avviene tramite un protocollo specifico che il server mette a disposizione tramite documentazione

#ESEMPIO:
#@app('/saluta', method=['GET'])
#def saluta_cliente():
#nome_cliente=request.args['nome_cliente']
#messaggio = f'Ciao, {nome_cliente}! '
#return jsonfy({'messaggio': messaggio})


#RESTFUL API
#Le API REST utilizzano richieste (o metodi) HTTP per dialogare con le risorse
# (GET, POST, PUT, HEAD, DELETE, PATCH, OPTIONS).
#L'archittetura rest è composta da vari vincoli

#1)Client-Server Architecture:
# l’architettura è composta da Client e Server, che comunicano tra loro tramite protocollo HTTP. Le parti agiscono in modo tra loro indipendente (ad esempio il Client non deve occuparsi del salvataggio delle informazioni, che rimangono nei singoli Server).

#2)Stateless:
#nessun contenuto Client è archiviato nel Server. Ciascuna richiesta dai vari Client contiene tutte le informazioni necessarie per richiedere il servizio.


#3)UNIFORM INTERFACE:
# Tutte le risorse sono accessibili attraverso un'interfaccia standard basata su standard come HTTP. Ciò semplifica l'architettura, migliorando la visibilità e semplificando l'interazione.



#ESEMPIO

# @app.route('/richiedi_nuove_credenziali', methods=['POST'])
# def richiedi_nuove_credenziali():
#     if request.method == 'POST':
#         if 'matricola' in session:
#             matricola = request.form['matricola_attuale']
#             email = request.form['email_studente']
#             nuova_matricola = request.form['nuova_Matricola']
#             nuova_email = request.form['nuova email']
#             if nuova_matricola == matricola or nuova_email==email:
#                return jsonify({'error': 'Matricola ed Email non possono essere uguali a quelle precedenti'})
#             cursor.execute('SELECT matricola,email,online FROM utenti WHERE email = %s AND matricola = %s',(email, matricola))
#             utente = cursor.fetchone()
#             if utente:
#                cursor.execute('UPDATE utenti SET matricola = %s, email = %s WHERE email = %s', (nuova_matricola, nuova_email, email))
#                conn.commit()
#                session['matricola'] = nuova_matricola
#                session['email']=nuova_email
#                                    # nuova_matricola = utente[0]
#                                     # email = utente[1]
#                online = utente[2]
#                return render_template('/utente.html', matricola=nuova_matricola, email=nuova_email, online=online)
#         if 'email_insegnante' in session:
#             email_istituzionale = request.form['email_insegnante']
#             nuova_email = request.form['nuova email']
#             password = request.form['password']
#             if nuova_email == email_istituzionale:
#                 return jsonify({'error': ' Email non può essere uguale a quella precedente'})
#             cursor.execute('SELECT nome,cognome,email_istituzionale FROM insegnanti WHERE email_istituzionale = %s',
#                            (email_istituzionale,))
#             user = cursor.fetchone()
#             if user:
#                 cursor.execute('UPDATE insegnanti SET email_istituzionale = %s WHERE email_istituzionale = %s',
#                                (nuova_email, email_istituzionale))
#
#                 conn.commit()
#                 session['email_insegnante'] = nuova_email
#
#                 cursor.execute('SELECT  nome, cognome, email_istituzionale FROM insegnanti')
#                 insegnanti_data = cursor.fetchall()
#                 return render_template('insegnanti.html', insegnanti=insegnanti_data)
#         error_message = 'L\'account non è loggato'
#         abort(404, description=error_message)


#In questo esempio l'API richiede un metodo post con la quale vengono inviati i dati per procedere all'aggiornamento delle nuove credenziali.
#Poi si recuperano i dati mediante request.form ossia si recuperano i dati relativi ai campi html.
#Poi si sviluppa la logica di aggiornamento delle credenziali(quindi aggiornamento database e gestione errori)



