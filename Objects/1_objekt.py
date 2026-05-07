class Auto():
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def starten(self):
        print(f"{self.marke} {self.modell} startet.")

    def stoppen(self):
        print(f"{self.marke} {self.modell} stoppt.")    
        
mein_auto = Auto("Volkswagen", "Golf", 2020)
print(mein_auto.marke) # This will print "Volkswagen"

Auto.starten(mein_auto) # This will print "Volkswagen Golf startet."
