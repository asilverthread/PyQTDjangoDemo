import json
import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from django_backend_proj.pyqt_desktop_demo import models
from django_backend_proj.pyqt_desktop_demo.models import Patient

if __name__ == "__main__":

    server = "cortese-crew-proof-of-concept-server.database.windows.net"
    database = "py-qt-django-demo"
    username = sys.argv[1]
    password = sys.argv[2]

    driver = '{ODBC Driver 17 for SQL Server}'

    odbc_str = 'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;UID=' + username + ';DATABASE=' + database + ';PWD=' + password
    connect_str = 'mssql+pyodbc:///?odbc_connect=' + odbc_str

    engine = create_engine(connect_str)
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()



    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    table = QTableWidget(15, 3)


    def refresh_table():
        table.clearContents()
        i = 0
        print("refreshing")
        for p in session.query(models.Patient).all():
            f = p.patient_first_name
            l = p.patient_last_name
            b = str(p.patient_birthdate)
            table.setItem(i, 0, QTableWidgetItem(f))
            table.setItem(i, 1, QTableWidgetItem(l))
            table.setItem(i, 2, QTableWidgetItem(b))
            i += 1


    layout.addWidget(table)
    refresh_table()
    table.show()
    fname = QLineEdit()
    lname = QLineEdit()
    bday = QDateEdit()
    layout.addWidget(fname)
    layout.addWidget(lname)
    layout.addWidget(bday)
    save = QPushButton("save")


    def on_save_clicked():
        print("starting")
        try:
            session.add(Patient(patient_first_name=fname.text(), patient_last_name=lname.text(), patient_birthdate=bday.date().toPyDate()))
        except Exception as e:
            print(e)
        refresh_table()


    save.clicked.connect(on_save_clicked)

    layout.addWidget(save)
    window.setLayout(layout)
    window.show()
    app.exec()
