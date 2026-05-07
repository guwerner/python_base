from random import randint

zahl = randint(a=1, b=100)
zahlRaten = 0

while zahlRaten != zahl:
    zahlRaten = int(input("Rate eine Zahl zwischen 1 und 100: "))
    if zahlRaten < zahl:
        print("Zu niedrig! Versuche es erneut.")
    elif zahlRaten > zahl:
        print("Zu hoch! Versuche es erneut.")
    else:
        print("Glückwunsch! Du hast die Zahl erraten.")
        

