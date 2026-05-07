leere_liste = []
print(leere_liste)
einkauszettel = ["Milch", "Brot", "Eier", "Käse"]
print(einkauszettel)
print(einkauszettel[0])
print(einkauszettel[2])

einkauszettel.append("Butter")
print(einkauszettel)

einkauszettel.insert(2, "Äpfel")
print(einkauszettel)
einkauszettel.append(["Zucker", "Salz"])
print(einkauszettel)
print(einkauszettel[6][0]) # Zugriff auf "Zucker" in der verschachtelten Liste
