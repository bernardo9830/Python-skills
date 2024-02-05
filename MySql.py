import mysql.connector
# creazione connessione
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pysql"
)
print(db)

#CREAZIONE DATABASE : cursor.execute("CREATE DATABASE universita")
# cursor = db.cursor() #Il cursore è un puntatore per lavorare sulle tabelle
# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS clienti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR (255), cognome VARCHAR(255))")
# # sql= "INSERT INTO clienti (nome,cognome) VALUES(%s,%s)" #Inserire i value
# # values=[("LUCA", "ROSSI"),       #Inserimento Valori multipli con lista di tuple.
# #          ("BERNARDO", "VALENTE"),
# #         ("LUISA", "SPAGNOLO")]
# # cursor.executemany(sql,values)  #Modifiche al database(con many utilizziamo più dati)
# # db.commit()               #Linea di codice che apporta le modifiche
# # print("id riga inserita",cursor.lastrowid)      #Ti stampa l'ultima riga dell'id
# sql = "SELECT id, cognome FROM clienti"    #Seleziona due colonne dalla lista clienti
# cursor.execute(sql)
# reslt = cursor.fetchall()   #Prende tutti i record delle colonne selezionate
# for riga in reslt:
#     print(riga)
#
# # sql1="SELECT id, nome FROM clienti WHERE nome= 'BERNARDO' "
# # cursor.execute(sql1)
# # result=cursor.fetchall()      #Seleziona tutti i record con un certo valore di nome.
# # for riga in result:
# #     print(riga)
#
# # sql2="SELECT*FROM clienti ORDER BY nome LIMIT 4" #ORDINA IN SENSO ALFABETICO E PONI UN LIMITE DI RIGHE DA VEDERE
# # cursor.execute(sql2)
# # result=cursor.fetchall()
# # for riga in result:
# #     print(riga)
#
# sql4 = " DELETE FROM CLIENTI WHERE nome ='BERNARDO'"   #Cancelliamo i record il cui nome ha un certo valore
# cursor.execute(sql4)
# db.commit()
# # print("NUMERO RIGHE CANCELLATE: ", cursor.rowcount)
# # sql5="UPDATE clienti SET nome = 'ORAZIO' WHERE id = 4"   #Aggiorna un record con dei nuovi valori
# # cursor.execute(sql5)
# # db.commit()
# # print("RIGHE MODIFICATE: ", cursor.rowcount)
# #
# # # # Aggiunta della colonna 'citta'
# # alter_query = "ALTER TABLE clienti ADD COLUMN città int"   #Aggiunta di un'altra colonna
# # cursor.execute(alter_query)
# # db.commit()
# # sql8 = "UPDATE clienti SET città = %s WHERE id = %s"   #Aggiorno i record che hanno un certo valore con un nuovo valore.
# # values = [
# #     (1, 1),
# #     (2, 2),
# #     (3, 3),
# #     (5, 4),
# #     (None, 6),
# #     (2, 7),
# #     (None, 10)
# # ]
# # cursor.executemany(sql8, values)
# # db.commit()
#
# # JOIN TABELLE
# #Unisce due tabelle per due chiavi specificate.(PRIMARY AND FOREIGN KEY)
# # cursor.execute("CREATE TABLE città (id int AUTO_INCREMENT PRIMARY KEY, nome_città VARCHAR(255))")
# # db.commit()
#
#
# # sql10= "INSERT INTO città (nome_città) VALUES (%s)"      #Inserire i value
# # values=[("Milano",), ("TORINO",), ("NAPOLI",), ("OLBIA",), ("CROTONE",)]
# # cursor.executemany(sql10, values)   #Modifiche al database(con many utilizziamo più dati)
# # db.commit()    #le esegue
#
# # sql= "INSERT INTO clienti (nome,cognome) VALUES(%s, %s)" #Inserire i value
# # values=("LUCA", "ROSSI")
# # cursor.execute(sql,values)#Modifiche al database(con many utilizziamo più dati)
# # db.commit()#le esegue
# sql_new = "SELECT nome, cognome, città.nome_città FROM clienti INNER JOIN città ON clienti.città=città.id"
# cursor.execute(sql_new)
# result=cursor.fetchall()
# for riga in result:
#     print(riga)
