import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


# QMainWindow different from base QWidget, contains status bar/menu
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle('Demo Application')
        self.resize(400, 300)
        self.statusBar().showMessage('Status bar text goes here.')
        self.setup_menu()
        dd_icon = QIcon('icons/devdungeon32x32.png')
        self.setWindowIcon(dd_icon)

    def setup_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        new_action = QAction('New', self)
        file_menu.addAction(new_action)
        file_menu.addSeparator()
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Quit the application.')
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu('Help')
        new_icon = QIcon('icons/devdungeon32x32.png')
        about_action = QAction(new_icon, 'About', self)
        about_action.setStatusTip("Learn more about this application.")
        help_menu.addAction(about_action)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = GUI()
    gui.show()

    sys.exit(app.exec_())
