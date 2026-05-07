dict1 = {}

dict2 = {"Name": "Alice", "Alter": 30, "Stadt": "Berlin"}

print(dict1)  # Ausgabe: {}
print(dict2["Name"])  # Ausgabe: Alice

 
for key in dict2:
    print(key, ":", dict2[key])
    
dict2["Beruf"] = "Entwicklerin"
print(dict2)