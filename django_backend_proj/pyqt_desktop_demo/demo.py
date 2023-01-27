import json

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from requests import Session

if __name__ == "__main__":
    djangoSession = Session()
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    for m in json.loads(djangoSession.get(url="http://127.0.0.1:8000/pyqt_django_demo/patients").content)["Patients"]:
        layout.addWidget(QLabel(str(m)))
    window.setLayout(layout)
    window.show()
    app.exec()
