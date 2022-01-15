list_dict=[]
class Annonce:
    def __init__(self,titre,ville,prix,date):
        self.titre=titre
        self.ville=ville
        self.prix=prix
        self.date=date
        
        if self.prix.endswith('DH'):
            self.prix=self.prix[ :-1][ :-1]
        else:
            pass
        
        

    def toDict(self):
        
        dict={}
        dict['titre']=self.titre
        dict['ville'] = self.ville
        dict['prix'] = self.prix
        dict['date'] = self.date
        list_dict.append(dict)
        return dict
    def show(self):
        print(self.toDict())