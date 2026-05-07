# Tupel lassen sich nicht verändern, sie sind unveränderlich (immutable)

# Erstellen eines Tupels
mein_tupel = (1, 2, 3, "Hallo", [4, 5], (6, 7))
print(mein_tupel)
mein_tupel[0] = 10 # This will raise a TypeError because tuples are immutable

