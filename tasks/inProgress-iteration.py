# Ogolnie to z takiego stringa:
# "3 5\n.....\n.*.*.\n....."
# Powinien wyjsc taki:
# "3 5\n.....\n.....\n....."

a = "3 5\n.....\n.*.*.\n.....".split()
print(a)
print(len(a[1]))
for i in range(len(a[2])):
    print(a[3][i:i+3].replace(".*.", "..."))

# Umiem to w locie zmienic, ale juz zastapic nie umiem
print(a)

