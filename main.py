import csv
from Avito import Avito
from Annonce import list_dict
from models import add_to_db 


myFile = open("annonces.csv","a",newline="",encoding='UTF-8')
headers = ['titre','ville','prix','date']
writer = csv.DictWriter(myFile,fieldnames=headers)
writer.writeheader()
page=1


while True:
    print("################## Page:",page)
    avito = Avito("https://www.avito.ma/fr/maroc/t%C3%A9l%C3%A9phones/%C3%A0_vendre="+str(page))
    avito.scrap()
    #avito.show()
    if avito.annonces==[]:
        break
    for annonce in avito.annonces:
        writer.writerow(annonce.toDict())
    page=page+1
    
add_to_db(list_dict)
print(list_dict)
myFile.close()
