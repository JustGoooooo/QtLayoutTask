from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
app = QApplication([])
G = QWidget()
G.show()

main_layout = QHBoxLayout()
main_layout2 = QHBoxLayout()
QV_layout = QVBoxLayout()

b1 = QPushButton("")
b2 = QPushButton("")
b3 = QPushButton("")
b4 = QPushButton("")
b5 = QPushButton("")

QV_layout.addLayout(main_layout)
QV_layout.addLayout(main_layout2)
main_layout.addWidget(b1)
main_layout.addWidget(b2)
main_layout.addWidget(b3)
main_layout2.addWidget(b4)
main_layout2.addWidget(b5)

G.setLayout(QV_layout)
app.exec()
