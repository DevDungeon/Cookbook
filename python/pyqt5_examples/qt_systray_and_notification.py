# Adapted from Evgenii Legotckoi https://evileg.com/en/post/68/
# https://www.youtube.com/watch?v=1_4jfqYOi6w
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    """
         Сheckbox and system tray icons.
         Will initialize in the constructor.
    """
    check_box = None
    tray_icon = None

    # Override the class constructor
    def __init__(self):
        # Be sure to call the super class method
        QMainWindow.__init__(self)


        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(self.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def quit(self):
        self.tray_icon.hide()
        qApp.quit()

    # Override closeEvent, to intercept the window closing event
    # The window will be closed only if there is no check mark in the check box
    def closeEvent(self, event):
        event.ignore()
        self.hide()

        self.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    #mw.show()
    sys.exit(app.exec())
