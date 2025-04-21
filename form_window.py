
from PyQt5 import QtCore, QtWidgets
from form import Ui_Dialog

class FormWindow(QtWidgets.QDialog):
    plan_saved = QtCore.pyqtSignal(dict)  # signal ke CalendarWindow

    def __init__(self, selected_date=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.selected_date = selected_date

        # Tampilkan tanggal di label
        if selected_date:
            self.ui.label_selectedDate.setText(selected_date.toString("yyyy-MM-dd"))

        # Tombol simpan dan batal
        self.ui.pushButton_2.clicked.connect(self.save_plan)
        self.ui.pushButton.clicked.connect(self.close)

    
    def save_plan(self):
        plan = {
            "name": self.ui.lineEdit.text(),
            "type": self.ui.comboBox.currentText(),
            "from": self.ui.timeEdit.time().toString("HH:mm"),
            "to": self.ui.timeEdit_2.time().toString("HH:mm"),
            "date": self.selected_date.toString("yyyy-MM-dd")
        }
        self.plan_saved.emit(plan)
        self.close()
