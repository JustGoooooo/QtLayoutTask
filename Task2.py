from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
app = QApplication([])
G = QWidget()
G.show()

main_layout = QHBoxLayout()
QV_layout = QVBoxLayout()

b1 = QPushButton("   ")
b2 = QPushButton("   ")
b3 = QPushButton("   ")
b4 = QPushButton("   ")
b5 = QPushButton("   ")

main_layout.addWidget(b1)
main_layout.addLayout(QV_layout)
main_layout.addWidget(b2)
QV_layout.addWidget(b3)
QV_layout.addWidget(b4)
QV_layout.addWidget(b5)

G.setLayout(main_layout)
app.exec()

