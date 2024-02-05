import mysql.connector

        
def __str__(self):
        return f"{self.nom} {self.prenom}"
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
curseur.execute("SELECT nom, prenom FROM employe ")

#récuperation des données
result= curseur.fetchone()

#affichage des données 
for capacite in result:
    print(f"La capacité de toute les salles est de {capacite} personne.")

#close curseur
curseur.close() 

#close connexion
connexion.close()