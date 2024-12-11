from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello from PyQt!")
label.show()
app.exec_()