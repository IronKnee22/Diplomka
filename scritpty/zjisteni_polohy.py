import geocoder

# Získání polohy podle IP adresy
g = geocoder.ip("me")  # 'me' zjistí vaši aktuální IP adresu
print(g.latlng)  # Vytiskne seznam [latitude, longitude]
print(g.address)  # Vytiskne adresu
