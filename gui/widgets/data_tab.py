from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidget


class SleepDataTab(QWidget):
    def __init__(self, ui, sleep_data_service):
        super().__init__()
        self.ui = ui
        self.sleep_data_service = sleep_data_service
        self.setup_table()
        self.connect_signals()

    def setup_table(self):
        self.ui.data_table_widget.setColumnCount(14)
        self.ui.data_table_widget.setHorizontalHeaderLabels([
            "ID", "Date", "RespId", "sleepStartTime", "SleepEndTime", "TotalSleepHours", "SleepQuality", "ExerciseMinutes", "CaffeineIntakeMg", "ScreenTime",
            "WorkHours", "ProductivityScore", "MoodScore", "StressLevel"
        ])
        self.ui.data_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.data_table_widget.setSelectionBehavior(QTableWidget.SelectRows)

    def connect_signals(self):
        self.ui.all_data_btn.clicked.connect(self.load_all)


    def load_all(self):
        pass