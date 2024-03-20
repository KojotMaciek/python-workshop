a = "3 5\n.....\n.*.*.\n.....".split("\n")
print(a)
for i, s in enumerate(a):
    a[i] = s.replace('*.*', '...')

print(a)

b = '\n'.join(a)
print(b)
