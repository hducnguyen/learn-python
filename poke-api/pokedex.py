# library, module, package = plugins/extension
import requests
# pip install requests  =>>  packet manager

print("Welcome to hduc's Pokedex")

HOME_ADDRESS = (" https://pokeapi.co/api/v2/pokemon/")
user_input = input('Enter a pokemon name or id: ')
URL = HOME_ADDRESS + user_input

response = requests.get(URL)
print(response)

# Response codes:
#     - 200-299 Succesful
#     - 400-499 Not found (404)
#     - 500 Server error

if response.status_code == 200:
    pokemon = response.json()
    # print(pokemon)
    print("Pokemon name: " + pokemon['name'])
    print("ID: " + str(pokemon['id']))
    print("Height: " + str(pokemon['height']) + 'cm')

    print("Type(s): ", end=" ")
    for type in pokemon['types']:
        print(type['type']['name'], end=", ")





else:
    print("Failed")