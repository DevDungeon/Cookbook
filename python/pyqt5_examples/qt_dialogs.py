import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit


class App(QWidget):
    def __init__(self):
        super().__init__()
        i, okPressed = QInputDialog.getInt(self, "Get integer", "text:", 28, 0, 100, 1)
        if okPressed:
            print(i)

        f, okPressed = QInputDialog.getDouble(self, "Get double", "Percentage:", 28.0, 0, 100.0, 1)
        if okPressed:
            print(f)

        items = ("Red", "Blue", "Green")
        item, ok = QInputDialog.getItem(self, "Get item", "Color:", items, 0, False)
        if ok and item:
            print(item)

        text, okPressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)

        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    # sys.exit(app.exec_())
