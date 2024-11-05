import requests

data = requests.get(
    "https://www.meteosource.com/api/v1/free/point?lat=50.135365&lon=14.104330&sections=all&timezone=Europe/Prague&language=en&units=metric&key=k0rqs4gyi4bgoicjizl42es2zux3y4kg1dvio6od"
)
data = data.json()

for i in range(24):
    print(
        f"Hodina {i} procento oblohy pokryté mraky : {data['hourly']['data'][i]['cloud_cover']['total']}%"
    )
pass
