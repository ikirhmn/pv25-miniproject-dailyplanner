
import sys
from PyQt5 import QtWidgets
from calendar_logic import CalendarWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
