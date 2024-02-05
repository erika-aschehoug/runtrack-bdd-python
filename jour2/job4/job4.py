import mysql.connector

#creation connexion a la base de donnée
connexion = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'root',
    database = 'LaPlateforme'
)

#creation du curseur
curseur = connexion.cursor()

#creation de la requete
curseur.execute("SELECT nom, capacite FROM salle")

#récupération des données
result = curseur.fetchall()

#affichage des données
for nom, capacite in result:
    print(f"Nom: {nom}, Capacité: {capacite}")

#fermeture du curseur
curseur.close()

#femeture de la connexion a la bdd
connexion.close()
