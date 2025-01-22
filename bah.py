import sys
import PySide6.QtWidgets

app = PySide6.QtWidgets.QApplication(sys.argv)

janela = PySide6.QtWidgets.QMainWindow()
central = PySide6.QtWidgets.QWidget()
layout = PySide6.QtWidgets.QVBoxLayout()
janela.setCentralWidget(central)

buton = PySide6.QtWidgets.QPushButton("Butao")
buton.setStyleSheet("font-size: 40px; color: red")
layout.addWidget(buton)

buton2 = PySide6.QtWidgets.QPushButton("Bah")
buton2.setStyleSheet("font-size: 40px; color: red")
layout.addWidget(buton2)

menu = janela.menuBar()
pmenu = menu.addMenu("Sei la")
pacao = pmenu.addAction("primeira acao")

status = janela.statusBar()
status.showMessage("Bah guri")

central.setLayout(layout)
janela.show()


app.exec()