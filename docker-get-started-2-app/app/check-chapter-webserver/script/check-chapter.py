import requests

url = "http://www.volonte-d.com/"
response = requests.get(url)

if "Chapitre 1089" in response.text:
    print("La chaîne 'Chapitre 1089' est présente sur la page.")
else:
    print("La chaîne 'Chapitre 1089' n'est pas présente sur la page.")