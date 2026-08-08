import requests

city = input(" ENTER CITY NAME : ")

URL = f"https://wttr.in/{city}?format=3"

response = requests.get(URL)

if response.status_code == 200:
    print(response.text)

else:
    print("Could not fetch Weather data. ") 

