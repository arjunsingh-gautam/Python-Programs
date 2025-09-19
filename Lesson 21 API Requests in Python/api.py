import requests # Module used to make API request
base_url="https://pokeapi.co/api/v2/" # Poki API

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url) # get() will return an response object
   # print(response) # Output:<Response [200]>  200 means a successful response
    if response.status_code == 200: #status_code: data member which store response status code
        print("Data Retrieved!")
        pokimon_data=response.json()        # json() method of response object used to convert json object to python dictionary
        # print(f"Pokimon Data:\n{pokimon_data}")
        return pokimon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
pokemon_name=input("Enter your pokimon name:").lower()
pokimon_info=get_pokemon_info(pokemon_name)

if pokimon_info:
    print("Details about pokimon")
    print(f"Name:{pokimon_info["name"]}")
    print(f"ID:{pokimon_info["id"]}")
    print(f"Height:{pokimon_info["height"]}")
    print(f"Weight:{pokimon_info["weight"]}")
