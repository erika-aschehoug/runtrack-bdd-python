import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.curseur = self.connexion.cursor()

    def ajout_employe(self, nom, prenom,salaire, id_service):
        requete = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeur = (nom, prenom, salaire, id_service)
        self.curseur.execute(requete, valeur)
        self.connexion.commit()

    def lire_employe(self,id):
        requete = "SELECT * FROM employe WHERE id = %s"
        self.curseur.execute(requete, (id))
        employe=self.curseur.fetchone()
        return employe
    
    def maj_employe(self, id, nom, prenom, salaire, id_service):
        requete="""
        UPDATE employe
        SET nom = %s, prenom = %s, salaire = %s, id_service = %s
        WHERE id = %s """
        valeurs = (nom, prenom, salaire, id_service, id)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def supprimer_employe(self, id):
        requete = "DELETE FROM employe WHERE id = %s"
        self.curseur.execute(requete, (id,))
        self.connexion.commit()     

    def fermer (self):
        self.curseur.close()
        self.connexion.close()

#Instance de la classe employe
entreprise = Employe('localhost', 'root', 'root', 'Entreprise')

#ajout d'un employé
entreprise.ajout_employe('Beaussaert', 'Valentin', 1500, 1)
print(entreprise.lire_employe(1))

# Verification que la modification a été réalisé
print(entreprise.lire_employe(1))

# suppression d'un employe
entreprise.supprimer_employe(1)

entreprise.fermer()

# Début du job07
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Entreprise",
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM employe WHERE salaire > 3000")

results = cursor.fetchall()
print(results)

cursor.execute("""SELECT employe.id, employe.nom, employe.prenom, service.nom FROM employe
               JOIN service
               ON employe.id_service = service.id""")

results = cursor.fetchall()
print (results)

cursor.close()
mydb.close()