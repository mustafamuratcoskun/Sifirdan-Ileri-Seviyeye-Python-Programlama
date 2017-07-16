import sys
from PyQt5 import  QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazı_alanı = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdır = QtWidgets.QPushButton("Yazdır")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addStretch()

        self.setLayout(v_box)


        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)



        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Temizle":
            self.yazı_alanı.clear()

        else:
            print(self.yazı_alanı.text())




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
