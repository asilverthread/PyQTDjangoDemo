import json

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from requests import Session

PATIENTS_URL = "http://127.0.0.1:8000/pyqt_django_demo/patients"

if __name__ == "__main__":
    djangoSession = Session()
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    table = QTableWidget(15, 3)


    def refresh_table():
        table.clearContents()
        i = 0
        print("refreshing")
        for res in json.loads(djangoSession.get(url=PATIENTS_URL).content)[
            "Patients"]:
            f = res["patient_first_name"]
            l = res["patient_last_name"]
            b = res["patient_birthdate"]
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
            d = {
                "patient_first_name": fname.text(),
                "patient_last_name": lname.text(),
                "patient_birth_date": str(bday.date().toPyDate())
            }
            print(d)
            djangoSession.post(url=PATIENTS_URL, data=json.dumps(d))
            print("done")
        except Exception as e:
            print(e)
        refresh_table()


    save.clicked.connect(on_save_clicked)

    layout.addWidget(save)
    window.setLayout(layout)
    window.show()
    app.exec()
