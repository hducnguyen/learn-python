import requests

base_URL = "https://valorant-api.com/v1/agents"

response = requests.get(base_URL)

data = response.json()
agents_list = data['data']

options = input("1 for all agents name, 2 for detailed data of 1 agent: ")
if options == "1":
    # for i in range(len(data["data"])):
    #     print(data["data"][i]["displayName"])
    for i, agent in enumerate(agents_list):
        print(f"{i+1}. {agent['displayName']}")
elif options == "2":
    agent_name = input("Enter the agent number/name")
    if agent_name.isnumeric():
        print(f"Agent No. {agents_list["data"].length()}")
    for i, agent in enumerate(agents_list):
        if 
