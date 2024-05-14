class Somme:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def Affiche_somme(self):
        return self.n1+ self.n2
calcule=Somme(4,6)
reponse=Somme.Affiche_somme(calcule)
print("la somme de deux nombres vont :",reponse)

