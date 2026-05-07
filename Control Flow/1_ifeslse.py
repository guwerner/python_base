x = int(input("Geben Sie eine ganze Zahl zwischen 1 und 20 ein: "))

y = "Kleiner 10"
z = "Größer 10"

if x < 10:
    print(y)
elif x > 10:
    print(z)
elif x == 10:
    print("Gleich 10")