# for i in range(2, 10):
#     print(i)

# for i in range(10, 1, -1):
#     print(i)

# num = 1
# while num < 10:
#     print(str(num) + ' < 10')
#     num += 1

# List / array: collection of the similar things

# food = ["pizza", "sushi", "bbq", "pho"]
# print(food[1] + ' is my most fav food')

# Elements inside a list have indices (index), start from 0 , [index]

# food[2] = "ramen"

# LIST METHODS: actions performed on a list

# food.append("spaghetti")

# food.insert(0, "com tam")

# food.remove("sushi")

# food.pop(2)

# print(food)

# Data structures: organize data: List vs Dictionary


# key-value pair

# car: xe hoi

# may tinh: computer

jack = {
    'name': 'Jack',
    'age': 14,
    'fav_game': 'aov',
    'friends': [
        {
            'name': 'Peter',
            'game': 'roblox aka adult game'
        },
        {
            'name': 'David',
            'game': 'roblox adopt me'
        }
    ]
}

jack['name'] = 'Duc'

jack['fav_food'] = ['sushi', 'ramen', 'com suon']

print(jack['friends'][0]['name'] + '\'s favorite game is ' + jack['friends'][0]['game'])


