print (10/ 3)
print (type(10 / 2)) # This will print the type of the result of the division, which is <class 'float'>

#Eingabe von Zahlen
num1 = int(input("Geben Sie die erste Zahl ein: "))

print (num1 + 1.1)

euro1 = float(input("Geben Sie den Betrag in Euro ein: "))
dollar1 = euro1 * 1.1 # Umrechnung von Euro in Dollar (angenommener Wechselkurs: 1 Euro = 1.1 Dollar)
print(f"{euro1} Euro entsprechen {dollar1} Dollar.")