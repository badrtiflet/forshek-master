from ctypes.wintypes import SIZE
from distutils.command.config import LANG_EXT
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import ModelAnnonces
from Avito import Avito as avito
import csv
from file_list import show as showlist, listmarque as marques

myFile = open("annonces.csv", "a", newline="", encoding='UTF-8')
headers = ['titre', 'ville', 'prix', 'date']
writer = csv.DictWriter(myFile, fieldnames=headers)
writer.writeheader()


class Fenetre(QDialog):
    def __init__(self):
        super(Fenetre, self).__init__()
        loadUi('UI/main.ui', self)
        self.tableWidget.setColumnWidth(0, 370)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.list_annonces = []
        self.fichiercsv.clicked.connect(self.message)
        self.page2.clicked.connect(self.go_to_page2)
        self.page3.clicked.connect(self.go_to_page3)
        self.loaddata()

    def loaddata(self):
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        annonces = session.query(ModelAnnonces).all()

        for annonce in annonces:
            self.list_annonces.append(vars(annonce))

        session.close()

        row = 0
        self.tableWidget.setRowCount(len(self.list_annonces))
        for annonce in self.list_annonces:
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(annonce["titre"]))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(annonce["ville"]))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(annonce["prix"]))
            self.tableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(annonce["date"]))
            row = row+1

    def message(self):
        test=[]

        for annonce in self.list_annonces:
            test.append({"titre":annonce["titre"],"ville":annonce["ville"],"prix":annonce["prix"],"date":annonce["date"]})
            writer.writerow(test)
        self.message = "Hello"
        print(self.message)
        
        
    def go_to_page2(self):
        page2= Page2()
        widget.addWidget(page2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print("page2 clicked :")
        
        
    def go_to_page3(self):
        page3 = Page3()
        widget.addWidget(page3)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
            
class Page2(QDialog):
    def __init__(self):
        super(Page2, self).__init__()
        loadUi('UI/page2.ui', self)
        self.main.clicked.connect(self.back_to_main)
        self.page3.clicked.connect(self.back_to_main)
        self.tableWidget.setColumnWidth(0, 370)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.marquelist.addItems(marques())
        self.marquelist.currentTextChanged.connect(self.chargervue)
        
    def chargervue(self,text):
        result = showlist(text)
        print(result)
        row = 0
        self.tableWidget.setRowCount(len(result))
        for annonce in result:
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(annonce["Ville"]))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(annonce["Annonces"])))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(str(annonce["Moyen de Prix"])))
            row += 1
                
    def back_to_main(self):
        main = Fenetre()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def back_to_page3(self):
        page3 = Page3()
        widget.addWidget(page3)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
class Page3(QDialog):
    def __init__(self):
        super(Page3, self).__init__()
        loadUi('UI/page3.ui', self)
        self.main.clicked.connect(self.back_to_main)
        self.page2.clicked.connect(self.back_to_page2)
        
        
    def back_to_main(self):
        main = Fenetre()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def back_to_page2(self):
        page2 = Page2()
        widget.addWidget(page2)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)
main = Fenetre()
page2= Page2()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.setFixedHeight(650)
widget.setFixedWidth(1000)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("xxxxx")
