def greet_1st_name(name):
    men = ["Kuba", "Barnaba"]
    if name in men:
        return "hi " + name
    if name[-1] == "a": 
        return "hi pretty " + name
    return "hi " + name

def greet(name):
    name_list = name.split(" ")
    first_name = name_list[0]
    greetings = greet_1st_name(first_name)
    name_list[0] = greetings
    return " ".join(name_list)

def test():
    assert greet("Maciek") == "hi Maciek"
    assert greet("Aga") == "hi pretty Aga"
    assert greet("Barnaba") == "hi Barnaba"
    assert greet("Kuba") == "hi Kuba"
    assert greet("Maciek Kowalski") == "hi Maciek Kowalski"
    assert greet("Aga Nowak") == "hi pretty Aga Nowak"
    assert greet("Barnaba Kowalczyk") == "hi Barnaba Kowalczyk"
    assert greet("Kuba Wojewodzki") == "hi Kuba Wojewodzki"

if __name__ == '__main__':
    test()