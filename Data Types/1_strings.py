x = "Hallo Welt!!!"
print(x[2]) # This will print the character at index 2, which is 'l'

print(x[:5]) # This will also print the substring from index 0 to 4, which is 'Hallo'
print(x[6:10]) # This will print the substring from index 6 to 9

y = "Dieser Text ist sehr lange, wie lange ist er?"
print(len(y)) # This will print the length of the string y

# Umwandlung von Zahl in Text
print("Hallo " + str(10))

' umwandeln von Text in großbuchstaben'
print(x.upper()) # This will convert the string x to uppercase and print it
# Umwandeln von Text in Kleinbuchstaben
print(x.lower()) # This will convert the string x to lowercase and print it

print(y.find("sehr")) # This will find the index of the substring "sehr" in the string y and print it