import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer

app = QApplication(sys.argv)
win = QWidget()
win.show()

# Initialize the timer
timer = QTimer()

# Specify which function to execute when timeout is reached
timer.timeout.connect(lambda: print("TIMEOUT HIT"))

# Start the timer with a timeout of 1 second.
# The timer will go on forever, triggering the
# timeout every second until it is stopped.
timer.start(1000)

# If you want to end it:
# timer.stop()

sys.exit(app.exec_())