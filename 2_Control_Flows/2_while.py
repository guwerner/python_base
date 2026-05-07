counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1    
    
eintscheidung = "ja" 
einkaufszettel = []
while eintscheidung == "ja":
    einkaufszettel.append(input("Was möchtest du kaufen? "))
    print("Willst du weitermachen? (ja/nein)")
    eintscheidung = input()       
    
print("Dein Einkaufszettel:", einkaufszettel)