import requests
import json

data = requests.get("https://spotovaelektrina.cz/api/v1/price/get-prices-json")
data = data.json()
print(json.dumps(data, indent=4))

hours_today = data.get("hoursToday", [])

# Zpracování jednotlivých hodin
for hour_data in hours_today:
    hour = hour_data.get("hour")
    price_eur = hour_data.get("priceEur")
    price_czk = hour_data.get("priceCZK")
    level = hour_data.get("level")
    
    print(f"Hodina: {hour}, Cena (EUR): {price_eur}, Cena (CZK): {price_czk}, Úroveň: {level}")