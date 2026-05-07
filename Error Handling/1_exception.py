eingabe = input("Geben Sie eine Zahl ein: ")

try:
    ergebnis = 10 / eingabe
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")
except TypeError:
    print("Fehler: Ungültiger Typ für die Division  .")  


    