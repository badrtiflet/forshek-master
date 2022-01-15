
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.sql import select

engine = create_engine('sqlite:///database.db')

connection = engine.connect()
metadata = db.MetaData()
tabe_avito = db.Table('avito', metadata, autoload=True, autoload_with=engine)
    
def listmarque():
    results = connection.execute(db.select([tabe_avito.columns.phone.distinct()]).order_by(db.asc(tabe_avito.columns.phone))).fetchall()
    list1 = []
    for i in results:
        list1.append(i[0])
    return list1

def show(marque):
    Query = connection.execute(select(tabe_avito).where(tabe_avito.columns.phone == marque))
    alll = Query.fetchall()
    Query.close()
    alll.sort(key=lambda x: x[3])
    varville = ""
    listresult=[]
    i = 0
    my_dict = {}
    for idx, row in enumerate(alll, start=1):
        if varville != str(row[3]) :
            if i > 0 :
                my_dict["Annonces"] = i
                if prixnum>0 :
                    my_dict["Moyen de Prix"] =prixtph/prixnum
                else:
                    my_dict["Moyen de Prix"] =0
                listresult.append(my_dict)
                my_dict = {}
            my_dict["Ville"] = str(row[3])
            varville = str(row[3])
            i = 0
            prixtph = 0
            prixnum = 0
        i += 1 
        if row[4] > 0 :
            prixtph += row[4]
            prixnum += 1
        if idx == len(alll) :
            my_dict["Annonces"] = i
            if prixnum>0 :
                my_dict["Moyen de Prix"] =prixtph/prixnum
            else:
                my_dict["Moyen de Prix"] =0
            listresult.append(my_dict)
            my_dict = {}    
    return listresult

#print(show("iPhone"))