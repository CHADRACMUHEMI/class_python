
class Etudiant:
    def __init__(self,nom,note1,note2):
        self.nom=nom
        self.note1=note1
        self.note2=note2
    def calc_moy(self):
        resultat=(self.note1+self.note2)/2
        return resultat
    def affiche(self):
        return self.nom
maintenant=Etudiant('kalumbi',3,7)
resultat=Etudiant.calc_moy(maintenant)
resultat2=Etudiant.affiche(maintenant)
print("votre nom est :",resultat2,"et vous avez la moyenne de :",resultat)
