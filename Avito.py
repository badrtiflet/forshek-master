import csv
import json
import re
from models import add_to_db
import requests
from bs4 import BeautifulSoup
from Annonce import Annonce

class Avito:
    def __init__(self,url):
        self.url=url
        self.annonces=[]
        myFile=open("parametres.json", "r")
        self.data =json.load(myFile)
        

    def scrap(self):
        page=requests.get(self.url)
        soup=BeautifulSoup(page.text,"html.parser")
        conteneur = soup.find("div",attrs={"class":self.data['conteneur']})
        if conteneur is None:
            return None
        annoncesHTML=conteneur.findAll("div",attrs={"data-testid":re.compile(self.data['annonce'])})
        for annonceHTML in annoncesHTML:
            annonce=self.createAnnonce(annonceHTML)
            self.annonces.append(annonce)

    def createAnnonce(self,annonceHTML):
        titre = annonceHTML.find("span",attrs={"class":self.data['titre']}).text
        prix = annonceHTML.find("span",attrs={"class":self.data['prix']}).text
        ville = annonceHTML.findAll("span", attrs={"class": "sc-1x0vz2r-0 kIeipZ"})[1].text
        date = annonceHTML.findAll("span",attrs={"class":"sc-1x0vz2r-0 kIeipZ"})[0].text
        annonce = Annonce(titre,ville,prix,date)
        return annonce
    def show(self):
        for annonce in self.annonces:
            annonce.show()
            
    
