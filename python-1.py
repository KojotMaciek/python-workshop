def greet_1st_name(name):
    men = ["Kuba", "Barnaba"]
    if name in men:
        return "hi " + name
    if name[-1] == "a": 
        return "hi pretty " + name
    return "hi " + name

def greet(name):
    first_name = name.split(" ")[0]
    return greet_1st_name(first_name)

print(greet("Maciek"))
print(greet("Aga"))
print(greet("Barnaba"))
print(greet("Kuba"))

print(greet("Maciek Kowalski"))
print(greet("Aga Nowak"))
print(greet("Barnaba Kowalczyk"))
print(greet("Kuba Wojewodzki"))