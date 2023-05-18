from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
app = QApplication([])
G = QWidget()
G.show()

main_layout = QHBoxLayout()

b1 = QPushButton("   ")
b2 = QPushButton("   ")
b3 = QPushButton("   ")

main_layout.addWidget(b1)
main_layout.addWidget(b2)
main_layout.addWidget(b3)


G.setLayout(main_layout)
app.exec()
