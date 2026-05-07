
def sayHello(name):
    print(f"Hello, {name}!")

sayHello("Alice")

def addNumbers(a,  b ):
    return a + b 

result = addNumbers(10, 15)
print(result)

def addieren(*zahlen):
    return sum(zahlen)

print(addieren(10, 20, 30, 23, 556))

def begruessung(name, alter):
    """ Diese Funktion begrüßt eine Person mit ihrem Namen und Alter."""
    print(f"Hallo {name}, du bist {alter} Jahre alt.")


begruessung("Bob", 25)