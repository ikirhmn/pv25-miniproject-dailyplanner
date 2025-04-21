
from PyQt5 import QtWidgets
from calendar_1 import Ui_MainWindow
from form_window import FormWindow

class CalendarWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Dict untuk menyimpan plan per tanggal
        self.plan_data = {}

        # Inisialisasi tanggal yang dipilih
        self.selected_date = self.ui.calendarWidget.selectedDate()

        # Event: ganti tanggal
        self.ui.calendarWidget.selectionChanged.connect(self.update_selected_date)

        # Event: tombol tambah ditekan
        self.ui.pushButton_3.clicked.connect(self.open_form)

        # Tampilkan plan awal
        self.show_plans_for_date(self.selected_date)

        # Tombol clear
        self.ui.pushButton.clicked.connect(self.clear_plans)

    def update_selected_date(self):
        self.selected_date = self.ui.calendarWidget.selectedDate()
        self.show_plans_for_date(self.selected_date)

    def open_form(self):
        self.form_window = FormWindow(self.selected_date)
        self.form_window.plan_saved.connect(self.receive_plan)
        self.form_window.exec_()

    def receive_plan(self, plan):
        date_str = plan["date"]
        if date_str not in self.plan_data:
            self.plan_data[date_str] = []
        self.plan_data[date_str].append(plan)
        self.show_plans_for_date(self.selected_date)

    def show_plans_for_date(self, date):
        self.ui.listWidget.clear()
        date_str = date.toString("yyyy-MM-dd")
        if date_str in self.plan_data:
            for plan in self.plan_data[date_str]:
                display = f"{plan['from']} - {plan['to']}: {plan['name']} ({plan['type']})"
                self.ui.listWidget.addItem(display)
        else:
            self.ui.listWidget.addItem("Belum ada plan untuk tanggal ini.")

    def clear_plans(self):
        date_str = self.selected_date.toString("yyyy-MM-dd")
        if date_str in self.plan_data:
            del self.plan_data[date_str]
        self.show_plans_for_date(self.selected_date)

