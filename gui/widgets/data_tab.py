import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QMessageBox

logger = logging.getLogger(__name__)

def create_int_item(value):
    item = QTableWidgetItem()
    item.setData(Qt.DisplayRole, value)
    return item

def parse_int_or_null(text):
        return 0 if not text.strip() else int(text)

def parse_float_or_null(text):
    return 0.0 if not text.strip() else float(text)

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
        #self.ui.data_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.data_table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        header = self.ui.data_table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)  # Позволяет изменять ширину
        header.setSectionsMovable(True)  # Разрешает перетаскивание столбцов

    def connect_signals(self):
        self.ui.all_data_btn.clicked.connect(self.load_all)

    def load_all(self):

        try:
            # Парсинг параметров из полей ввода
            respondent_id = parse_int_or_null(self.ui.search_id_resp.text())
            sl_start_time_start = parse_float_or_null(self.ui.sl_start_time_start.text())
            sl_start_time_end = parse_float_or_null(self.ui.sl_start_time_end.text())
            sl_end_time_start = parse_float_or_null(self.ui.sl_end_time_start.text())
            sl_end_time_end = parse_float_or_null(self.ui.sl_end_time_end.text())
            sl_total_time_start = parse_float_or_null(self.ui.sl_total_time_start.text())
            sl_total_time_end = parse_float_or_null(self.ui.sl_total_time_end.text())
            sl_quality_start = parse_int_or_null(self.ui.sl_quality_start.text())
            sl_quality_end = parse_int_or_null(self.ui.sl_quality_end.text())
            exercise_start = parse_int_or_null(self.ui.exercise_start.text())
            exercise_end = parse_int_or_null(self.ui.exercise_end.text())
            coffee_start = parse_int_or_null(self.ui.coffee_start.text())
            coffee_end = parse_int_or_null(self.ui.coffee_end.text())
            screen_time_start = parse_int_or_null(self.ui.screen_time_start.text())
            screen_time_end = parse_int_or_null(self.ui.screen_time_end.text())
            work_time_start = parse_float_or_null(self.ui.work_time_start.text())
            work_time_end = parse_float_or_null(self.ui.work_time_end.text())
            productivity_start = parse_int_or_null(self.ui.productivity_start.text())
            productivity_end = parse_int_or_null(self.ui.productivity_end.text())
            mood_start = parse_int_or_null(self.ui.mood_start.text())
            mood_end = parse_int_or_null(self.ui.mood_end.text())
            stress_start = parse_int_or_null(self.ui.stress_start.text())
            stress_end = parse_int_or_null(self.ui.stress_end.text())



            # Получение данных через сервис
            sleep_data = self.sleep_data_service.get_sleep_data_with_parameters(
                respondent_id,
                sl_start_time_start,
                sl_start_time_end,
                sl_end_time_start,
                sl_end_time_end,
                sl_total_time_start,
                sl_total_time_end,
                sl_quality_start,
                sl_quality_end,
                exercise_start,
                exercise_end,
                coffee_start,
                coffee_end,
                screen_time_start,
                screen_time_end,
                work_time_start,
                work_time_end,
                productivity_start,
                productivity_end,
                mood_start,
                mood_end,
                stress_start,
                stress_end
            )

            if not sleep_data:
                QMessageBox.information(self, "Информация", "Данные с такими параметрами не найдены")
                self.ui.data_table_widget.setRowCount(0)
            else:
                QMessageBox.information(self, "Успех", f"Загружено {len(sleep_data)} записей.")
                logger.info(f"Успешная загрузка данных. Загружено {len(sleep_data)} записей")
                self.load_table(sleep_data)

        except Exception as ex:
            error_msg = f"Непредвиденная ошибка: {str(ex)}"
            QMessageBox.critical(self, "Ошибка", error_msg)
            logger.error(error_msg)



    def load_table(self, sleep_data):
        self.ui.data_table_widget.setRowCount(0)
        self.ui.data_table_widget.setRowCount(len(sleep_data))
        for row, data in enumerate(sleep_data):
            # ID
            self.ui.data_table_widget.setItem(row, 0, create_int_item(data.id))

            date_str = data.sleep_date.strftime("%Y-%m-%d") if data.sleep_date else ""
            self.ui.data_table_widget.setItem(row, 1, QTableWidgetItem(date_str))

            self.ui.data_table_widget.setItem(row, 2, create_int_item(data.person_id))

            # Время начала сна (форматируем float)
            self.ui.data_table_widget.setItem(row, 3, QTableWidgetItem(f"{data.sleep_start_time:.2f}"))

            self.ui.data_table_widget.setItem(row, 4, QTableWidgetItem(f"{data.sleep_end_time:.2f}"))

            self.ui.data_table_widget.setItem(row, 5, QTableWidgetItem(f"{data.total_sleep_hours:.2f}"))

            self.ui.data_table_widget.setItem(row, 6, create_int_item(data.sleep_quality))

            self.ui.data_table_widget.setItem(row, 7, create_int_item(data.exercise_minutes))

            self.ui.data_table_widget.setItem(row, 8, create_int_item(data.caffeine_intake_mg))

            self.ui.data_table_widget.setItem(row, 9, create_int_item(data.screen_time_before_bed))

            self.ui.data_table_widget.setItem(row, 10, QTableWidgetItem(f"{data.work_hours:.2f}"))

            self.ui.data_table_widget.setItem(row, 11, create_int_item(data.productivity_score))

            self.ui.data_table_widget.setItem(row, 12, create_int_item(data.mood_score))

            self.ui.data_table_widget.setItem(row, 13, create_int_item(data.stress_level))

            # Настройки таблицы
        self.ui.data_table_widget.setSortingEnabled(True)
        self.ui.data_table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.data_table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
