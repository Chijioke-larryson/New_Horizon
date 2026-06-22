names = 'Larryson Chijioke'
print(names[0])  # L
print(names[1])  # a
print(names[2])  # r
print(names.replace('o', 'a'))  # Larrysan Chijiake   


# print(names.replace('o', 'a'))

for i in range(len(names)):
    print(i, names[i])


for name in names:
    print(name.upper(), end=' ')