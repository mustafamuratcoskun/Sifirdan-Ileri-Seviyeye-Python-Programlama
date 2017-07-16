import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
    def  init_ui(self):

        self.yazı_alanı = QtWidgets.QLabel("Bana henüz tıklanmadı..")
        self.buton = QtWidgets.QPushButton("Bana Tıkla")
        self.say = 0


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()


        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.buton.clicked.connect(self.click)

        self.show()
    def click(self):
        self.say += 1
        self.yazı_alanı.setText("Bana " + str(self.say) + " defa tıklandı.")





app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

