# Example modified from https://evileg.com/en/post/68/
# https://www.youtube.com/watch?v=1_4jfqYOi6w
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QAction, QMenu, QStyle, qApp
from PyQt5 import QtGui


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.tray_icon = QSystemTrayIcon(self)

        # Set icon to a standard or custom icon
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        # self.tray_icon.setIcon(QtGui.QIcon("icons/devdungeon32x32.png"))

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)

        tray_menu = QMenu()
        tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(tray_menu)  # Set right-click menu
        self.tray_icon.show()

    def notify(self, message):
        """Generate a desktop notification"""
        self.tray_icon.showMessage("Pssst!",
                                   message,
                                   QSystemTrayIcon.Information,
                                   3000)

    def exit_app(self):
        self.tray_icon.hide()  # Do this or icon will linger until you hover after exit
        qApp.quit()

    def closeEvent(self, event):
        """
        By overriding closeEvent, we can ignore the event and instead
        hide the window, effectively performing a "close-to-system-tray"
        action. To exit, the right-click->Exit option from the system
        tray must be used.
        """
        event.ignore()
        self.hide()
        self.notify("App minimize to system tray.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
