import sys

from PySide2.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication([])
    label = QLabel("Qt for Python !")
    label.show()
    sys.exit(app.exec_())