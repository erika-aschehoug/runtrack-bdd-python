import mysql.connector

#Création de la connexion à la base de données
connexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='LaPlateforme'
)

#Création du curseur
curseur = connexion.cursor()   

#Création de la requête
curseur.execute("SELECT * FROM etudiant")

#Récupération des données
result = curseur.fetchall()

#Affichage des données
for etudiant in result:
    print(etudiant)

#Fermeture du curseur
curseur.close()

#Fermeture de la connexion
connexion.close()