# def add(a, b):
#     answer = a + b
#     print("Answer: " + str(answer))

# add(4, 69)

def getNationality(country):
    if country == 'france':
        return 'french'
    elif country == 'vietnam':
        return 'vietnamese'
    elif country == 'japan':
        return 'japanese'
    elif country == 'china':
        return 'chinese'
    elif country == 'america':
        return 'american'

n1 = getNationality('france')
n2 = getNationality('vietnam')
n3 = getNationality('japan')
n4 = getNationality('china')
n5 = getNationality('america')

print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

# def add(a, b):
#     # return a + b
#     total = a + b
#     return total   

# print(add(5, 4))
# answer1 = add(6, 7)
# print(answer1)