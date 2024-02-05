import mysql.connector

#connexion bdd
connexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='LaPlateforme'
)

#création curseur
curseur= connexion.cursor()

#creation de la requete
curseur.execute("SELECT SUM(superficie) FROM etage" )

#récuperation des données
result= curseur.fetchone()

#affichage des données 
for superficie in result:
    print(f"La superficie de La Plateforme est de {superficie}m2.")

#close curseur
curseur.close() 

#close connexion
connexion.close()