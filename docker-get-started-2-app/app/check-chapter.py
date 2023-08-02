import requests

url = "http://www.volonte-d.com/"
response = requests.get(url)

if "Oda" in response.text:
    print("La chaîne 'Oda' est présente sur la page.")
else:
    print("La chaîne 'Oda' n'est pas présente sur la page.")