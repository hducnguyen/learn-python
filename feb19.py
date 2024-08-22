import requests

base_url = 'https://pokeapi.co/api/v2/pokemon/'

userInput = input("Enter an id or a pokemon name: ")

URL = base_url + userInput
response = requests.get(URL)

# print(response)

if response.ok:
    content =  response.json()
    name = content['forms'][0]['name']
    id = content['id']
    print("Name: " +  name.title())
    print("Id: " + str(id))
else:
    print(response)