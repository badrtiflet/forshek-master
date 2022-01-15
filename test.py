from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout,QPushButton,QComboBox
import sys
import sqlalchemy as db
from sqlalchemy import create_engine
 
engine = create_engine('sqlite:///database.db')
 
connection = engine.connect()
metadata = db.MetaData()
tabe_avito = db.Table('avito', metadata, autoload=True, autoload_with=engine)

def listville():
    results = connection.execute(db.select([tabe_avito.columns.ville.distinct()]).order_by(db.asc(tabe_avito.columns.ville))).fetchall()
    list1 = []
    for i in results:
        list1.append(i[0])
    return list1

class lineEditPrix(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.e2 = QLineEdit()
                self.e3 = QLineEdit()
                self.e4 = QComboBox()
                self.e4.addItems(listville())
                self.pybutton = QPushButton('OK', self)
                self.pybutton.clicked.connect(self.clickMethod)
                
                flo = QFormLayout()
                flo.addRow("Max",self.e2)
                flo.addRow("Min",self.e3)
                flo.addRow("Ville",self.e4)
                flo.addRow(self.pybutton)
                

                self.setLayout(flo)
                self.setWindowTitle("Prix")

        def clickMethod(self):
            txtprix = self.e2.text()
            if txtprix.isdigit():
                max = int(txtprix)
            else:
                print("Max not Number")
                return
            txtprix = self.e3.text()
            if txtprix.isdigit():
                min = int(txtprix)
            else:
                print("Min not Number")
                return
            if max<=min:
                print("Min Not Samll than Max")
                return
            choixville = self.e4.currentText()
            sql = "SELECT * FROM avito WHERE prix >= '%s' AND prix <='%s' AND ville ='%s' " % (min, max, choixville,)
            result = connection.execute(sql)
            for i in result:
                print(i)
                
if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = lineEditPrix()
        win.show()
        sys.exit(app.exec_())