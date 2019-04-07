PyQt5 Notes
===========


Installation
------------

Install PyQt5 package with:

    python -m pip install pyqt5
    
Install the designer from https://www.qt.io/download-qt-installer


Convert a designer file to Python file
--------------------------------------

    pyuic5 templates/main_window.ui -o main_window.py


Threading
---------

Use QThreads.

Create a class and subclass `QThread`.

Create a signal(channel) using `pyqtSignal` and specify what it should expect:

    done_signal = pyqtSignal(str)

Tie the done signal to a function in the calling object

    thread.done_signal.connect(func_name)

And then in the QThread class call emit:

    self.done_signal.emit(output_value)

If the thread is called in a short-lived function, store the thread in
an object or somewhere where it won't get garbage collected before
it finishes running.

Packaging
---------

Use [PyInstaller](https://www.pyinstaller.org/) to create standalone packages.

    python -m pip install pyinstaller
    pyinstall myapp.py
  
Dialogs
-------

There are a few [dialog](https://doc.qt.io/qt-5/qdialog.html) options:

    QInputDialog.get{Int,Double,Item,Text}()
    QColorDialog
    QFileDialog
    QFontDialog
    QInputDialog
    QMessageBox.{question,etc}()
    QWizard
    QErrorMessage


SysTray
-------

- https://evileg.com/en/post/68/
- https://www.youtube.com/watch?v=1_4jfqYOi6w

Create a `QSystemTrayIcon`, then call `set_icon()` on it and then `show()`.

Create a `QMenu`, call `addAction` to add `QAction`s that have been connected to a callback using `action.triggered.connect(func_name)`

References
----------

https://github.com/DevDungeon/PyQt5-Bitcoin-Price-Checker
https://github.com/DevDungeon/PyQt5-Bitcoin-Price-Checker/pull/1
