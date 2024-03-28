import string

def makeDiamond(letter):
    index = string.ascii_uppercase.index(letter)
    if letter == "A":
        return letter
    else:
        a = " "*index + "A"
        item= ""
        for i in range(1, index + 1):
            l = string.ascii_uppercase[i]
            item += " "*(index - i) + l + " "*(i*2 - 1) + l + "\n"
        half_diamond = (a + "\n" + item).split('\n')
        half_diamond_2nd = half_diamond[:-2]
        half_diamond_2nd.reverse()

        return "\n".join(half_diamond[:-1] + half_diamond_2nd)
    
if __name__ == '__main__':
    with open('diamond.txt', 'r') as file:
        print(file.read())
    print(makeDiamond(input("Please provide singe uppercase letter: ")))