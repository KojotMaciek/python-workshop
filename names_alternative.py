def greet_1st_name(name):
    men = ["Kuba", "Barnaba"]
    if name not in men and name[-1] == "a": 
        return "hi pretty "
    return "hi "

def greet(name):
    first_name = name.split(" ")[0]
    greetings = greet_1st_name(first_name)
    return greetings + name

if __name__ == '__main__':
    print(greet("Maciek"))
    print(greet("Aga"))
    print(greet("Barnaba"))
    print(greet("Kuba"))
    print(greet("Maciek Kowalski"))
    print(greet("Aga Nowak"))
    print(greet("Barnaba Kowalczyk"))
    print(greet("Kuba Wojewodzki"))