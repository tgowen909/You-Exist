import sys
# 1. Import QApplication and all the required widgets
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel, 
    QLineEdit, 
    QVBoxLayout,
    QPushButton
)
from functools import partial

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("Balls McGee")
window.setGeometry(100, 100, 100, 100)
#helloMsg = QLabel("Hello, World!", parent=window)
#helloMsg.move(5, 15)
#helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
#helloMsg.move(10, 20)

#typebitch = QLineEdit(parent=window)
#typebitch.move(5,50)


layout = QVBoxLayout()
#layout.addWidget(QPushButton("Top"))
#layout.addWidget(QPushButton("Center"))
#layout.addWidget(QPushButton("Bottom"))
layout.addWidget(QLabel("hi there", parent=window))
layout.addWidget(QLabel("hi there", parent=window))
layout.addWidget(QLabel("hi there", parent=window))
layout.addWidget(QLabel("hi there", parent=window))
layout.addWidget(QLabel("hi there", parent=window))
layout.addWidget(QLabel("hi there", parent=window))
layout.addWidget(QLabel("hi there", parent=window))
layout.addWidget(QLabel("hi there", parent=window))
layout.addWidget(QLabel("hi there", parent=window))


window.setLayout(layout)


# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())