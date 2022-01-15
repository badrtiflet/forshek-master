import sqlalchemy as db
from sqlalchemy import create_engine
 
engine = create_engine('sqlite:///database.db')
 
connection = engine.connect()
metadata = db.MetaData()
 
def dirham(montant):
    montant = montant.replace(" ", "")
    montant = montant.replace("DH", "")
    if montant.isdigit():
        return(int(montant))
    return 0
 
def marque(txt):
    x = txt.upper()
    if x.find("INFINIX") >= 0 :
        return "Infinix"
    if x.find("IPHONE") >= 0 :
        return "iPhone"
    if x.find("NOVA") >= 0 :
        return "Nova"
    if x.find("NOKIA") >= 0 :
        return "nokia"
    if x.find("XIAOMI") >= 0 :
        return "Xiaomi"
    if x.find("SAMSUNG") >= 0 :
        return "Samsung"
    if x.find("HUAWEI") >= 0 :
        return "Huawei"
    if x.find("REDMI") >= 0 :
        return "Redmi"
    if x.find("OPPO") >= 0 :
        return "Oppo"
    if x.find("SAMSANG") >= 0 :
        return "Samsung"
    if x.find("IPHONE") >= 0 :
        return "iPhone"
    if x.find("TECNO") >= 0 :
        return "Tecno"
    if x.find("SUMSUNG") >= 0 :
        return "Samsung"
    if x.find("HWAWI") >= 0 :
        return "Huawei"
    if x.find("NOTE 10") >= 0 :
        return "Samsung"
    if x.find("NOTE10") >= 0 :
        return "Samsung"
    if x.find("NOT 10") >= 0 :
        return "Samsung"
    if x.find("I PHONE") >= 0 :
        return "iPhone"
    if x.find("VIVO") >= 0 :
        return "Vivo"
    if x.find("NOTE 9") >= 0 :
        return "Samsung"
    if x.find("MI 9") >= 0 :
        return "Xiaomi"
    if x.find("REDME 9") >= 0 :
        return "Xiaomi"
    if x.find("NOTE4") >= 0 :
        return "Samsung"
    if x.find("ZENFONE 4") >= 0 :
        return "Asus"
    if x.find("13 PRO") >= 0 :
        return "iPhone"
    if x.find("NOTE20") >= 0 :
        return "Samsung"
    return "Indéfini"
 
sql = 'DROP TABLE IF EXISTS avito;'
result = connection.execute(sql)
sql = '''CREATE TABLE [avito] (
    [id] INTEGER  NOT NULL,
    [phone] VARCHAR(200)  NULL,
    [titre] VARCHAR(200)  NULL,
    [ville] VARCHAR(200)  NULL,
    [prix] INTEGER  NULL,
    [date] VARCHAR(200)  NULL);'''
result = connection.execute(sql)
tabe_avito = db.Table('avito', metadata, autoload=True, autoload_with=engine)
 
 
def alimentatiom():
    census = db.Table('annonces', metadata, autoload=True, autoload_with=engine)
    query = db.select([census]) 
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    #Inserting record one by one
    for x in ResultSet:
        print(x)
        y = marque(x[1])
        query = db.insert(tabe_avito).values(id=x[0],
                                             phone=y, titre=x[1], ville=x[2], prix=dirham(x[3]), date=x[4])
        connection.execute(query)
        print(query)
 
alimentatiom()