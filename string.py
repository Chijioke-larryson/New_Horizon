names = 'Larryson Chijioke'
print(names[0])  # L
print(names[1])  # a
print(names[2])  # r
print(names.replace('o', 'aa'))  # Larrysan Chijiake   


# print(names.replace('o', 'a'))

# for i in range(len(names)):
#     print(i, names[i])


# for name in names:
#     print(name.upper(), end=' ')


s = input('Enter your username:     ')

if s.isalpha():
    print('Your username is valid')
if not s.isalpha():
    print('Your username is invalid')


name = 'Larryson Chijioke'
School = 'New Horizon Computer Learning Center'
address = 'No 1, New Horizon Street, Off Admiralty Way, Lekki Phase 1, Lagos'

# 'My name is' "+ name + "'I am a student of' "+ School +"" 'My address is' + address

print('my name is \"' + name + '\" I am a student of \"' + School + '\" My address is \"' + address + '\"')