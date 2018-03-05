import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
win = QWidget()

win.setWindowTitle('Demo Application')
win.resize(400, 300)

win.show()

sys.exit(app.exec_())
