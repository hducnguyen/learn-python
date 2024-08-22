# Dictionary: data structure with a KEY-VALUE pair

# word: definition

# student_list =['Bao', 'Duc', 'Nguyen', 'Peter', 'Khoi']]
# index of 'Duc' = 1

# food_by_country ={
     # key    : value
#     "vietnam": 'pho', # field / entry : a pair of key-value
#     'japan': 'sushi',
#     'korea': 'tobokki',
#     'italy': 'pizza',
#     'america': 'burger'
# }

# country = input('Where do you want to go to: ')
# if country in food_by_country.keys():
#     print(f"I want to travel to {country} because it has {food_by_country[country]}")
# else:
#     print(f"I have not been to {country}")

# Can also combine Dictionary + List, Dictionary + Dictionary, Dictionary + Dictionary + List

countries = {
    'vietnam': {
        'capital': 'Hanoi',
        'population': '97mil',
        'cities': ['Ho Chi Minh', 'Danang', 'Vung tau', 'Dalat']
    },
    'japan': {
        'capital': 'Tokyo',
        'population': '125mil',
        'cities': ['Hiroshima', 'Osaka', 'Nagasaki']
    }
}

print(f"{countries['japan']['cities'][0]} and {countries['japan']['cities'][2]}")