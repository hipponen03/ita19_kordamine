class Laul:
    def __init__(self, pealkiri, laulja):
        self.pealkiri = pealkiri
        self.laulja = laulja

laul1 = Laul()
laul1.pealkiri = "Für Oksana"
laul1.laulja = "Nublu"

print("Laulu pealkiri on " + laul1.pealkiri + " ja laulab " + laul1.laulja)