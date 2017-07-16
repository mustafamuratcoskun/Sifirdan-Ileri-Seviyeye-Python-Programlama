import sys

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.radio_yazisi = QLabel("Hangi dili daha çok seviyorsun ?")

        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("Php")

        self.yazi_alani = QLabel("")

        self.buton = QPushButton("Gönder")

        v_box = QVBoxLayout()

        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazi_alani))

        self.setWindowTitle("Radio Button")

        self.show()

    def click(self,python,java,php,yazi_alani):
        if python:
            yazi_alani.setText("Python")
        if php:
            yazi_alani.setText("Php")
        if java:
            yazi_alani.setText("Java")


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
