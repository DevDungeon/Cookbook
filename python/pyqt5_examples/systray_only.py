# Example modified from https://evileg.com/en/post/68/
# https://www.youtube.com/watch?v=1_4jfqYOi6w
import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QAction, QMenu, QStyle, qApp
from PyQt5 import QtGui


class TrayOnlyApp(QSystemTrayIcon):

    def __init__(self):
        QSystemTrayIcon.__init__(self)

        self.setIcon(QtGui.QIcon("icons/devdungeon32x32.png"))

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)

        tray_menu = QMenu()
        tray_menu.addAction(exit_action)
        self.setContextMenu(tray_menu)  # Set right-click menu
        self.show()
        self.notify('Now running...')

    def notify(self, message):
        """Generate a desktop notification"""
        self.showMessage("Pssst!",
                         message,
                         QSystemTrayIcon.Information,
                         3000)

    def exit_app(self):
        self.tray_icon.hide()  # Do this or icon will linger until you hover after exit
        qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tray_app = TrayOnlyApp()
    sys.exit(app.exec())
