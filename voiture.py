from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, essence):
        self._essence = essence

    @property
    #getter
    def afficher_reservoir(self):
        return self._essence

    @abstractmethod
    def rouler(self, kilometre):
        pass

    @abstractmethod
    def faire_le_plein(self):
        pass

class Voiture(Vehicule):
    
    def __init__(self, essence = 50):
        super().__init__(essence)

    def essence_restante(self):
        print(f"Il vous reste {self.afficher_reservoir}L dans votre réservoir.")

    def rouler(self, kilometre):
        if self._essence < (kilometre * 8) / 100:
            print(f"Vous n'avez plus d'essence pour parcourir {saisie2} kms, faites le plein ! \n")
            return

        self._essence -= (kilometre * 8) / 100

        if self._essence < 10:
            print("Vous n'avez bientôt plus d'essence ! ")

        self.essence_restante()

    def faire_le_plein(self):
        self._essence = 50
        print("Vous pouvez repartir ! \n")

ma_voiture = Voiture()

while True:
    print("1: rouler     2: faire de l'essence       3: Afficher réservoir \n")
    saisie = input("Que voulez-vous faire? ")
    if saisie not in ["1", "2", "3"]:
        print("Écrire 1, 2 ou 3 \n")
        continue

    if saisie == "1":
        saisie2 = input("Entrez le nombre de km à parcourir : \n")
        saisie2 = int(saisie2)
        ma_voiture.rouler(saisie2)

    if saisie == "2":
        ma_voiture.faire_le_plein()

    if saisie == "3":
        ma_voiture.essence_restante()