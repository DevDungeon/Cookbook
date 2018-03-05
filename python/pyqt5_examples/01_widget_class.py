import sys
from PyQt5.QtWidgets import QApplication, QWidget


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle('Demo Application')
        self.resize(400, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = GUI()
    gui.show()

    sys.exit(app.exec_())
