import json

myFile = open("parametres.json", "r")
data = json.load(myFile)
print(data['conteneur'])