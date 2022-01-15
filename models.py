from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, create_session


engine = create_engine('sqlite:///database.db')
Base = declarative_base()


annonces = [{'titre': 'Samsung Galaxy A12 128-4go', 'ville': 'Casablanca', 'prix': '1 650 DH', 'date': '27 Décembre'},    
            {'titre': 'Samsung galaxy S21 5G 256-8go', 'ville': 'Casablanca', 'prix': '7 100 DH', 'date': '27 Décembre'},
            {'titre': 'Samsung Galaxy A72 256/8Go', 'ville': 'Casablanca', 'prix': '4 300 DH', 'date': '21 Décembre'},
            {'titre': '6s à vendre très bon état ', 'ville': 'Fès', 'prix': '750 DH', 'date': '12 Décembre'},
            {'titre': 'Samsung Galaxy A03s 64Go 4Go RAM', 'ville': 'Casablanca', 'prix': '1 399 DH', 'date': '26 Novembre'},
            {'titre': 'SAMSUNG S9 NOIR 64 Go avec Carte SD 16 Go', 'ville': 'Casablanca', 'prix': '10 DH', 'date': '24 Août'},]

class ModelAnnonces(Base):
    __tablename__ = "annonces"
    id = Column(Integer, primary_key=True,autoincrement=True)
    titre = Column(String(200))
    ville=Column(String(200))
    prix = Column(String(30))
    date=Column(String(200))
    

session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session=session()

class ModelAvito(Base):
    __tablename__ = "avito"
    id = Column(Integer, primary_key=True,autoincrement=True)
    phone = Column(String(200))
    titre = Column(String(200))
    ville=Column(String(200))
    prix = Column(String(30))
    date=Column(String(200))
    
session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session=session()
def add_to_db(annonces):
    for annonce in annonces:
                field = ModelAnnonces()
                
                
                field_titre = [r.titre for r in session.query(ModelAnnonces.titre)]
                field_prix = [r.prix for r in session.query(ModelAnnonces.prix)]
                field_ville = [r.ville for r in session.query(ModelAnnonces.ville)]
                field_date = [r.date for r in session.query(ModelAnnonces.date)]
                if annonce['titre']  in  field_titre and annonce['prix']  in field_prix and annonce['ville']  in field_ville and annonce['date'] in  field_date :
                    pass
                    print(" hade  lfilter  khedam !!!!!")
                else:
                    field.titre=annonce['titre']
                    field.ville=annonce['ville']
                    field.prix=annonce['prix']
                    field.date=annonce['date']
                    session.add(field)
                    session.commit()
                    print('hada  li bedelti !!!!!')
                    
                session.close()
                
                
