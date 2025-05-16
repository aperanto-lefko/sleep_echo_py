from PySide6.QtWidgets import QTableWidget, QMessageBox, QTableWidgetItem, QWidget, QHeaderView
from PySide6.QtCore import Qt


class RespondentTable(QWidget):
    def __init__(self, table_widget, respondent_service):
        super().__init__()
        self.table = table_widget
        self.respondent_service = respondent_service
        self.initialize_table()

    def initialize_table(self):
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "ID", "First Name", "Last Name", "Email", "Gender", "Country", "Age"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSortingEnabled(True)  # Включает сортировку таблицы по клику на заголовки колонок
        self.table.setSelectionBehavior(
            QTableWidget.SelectRows)  # Устанавливает выделение целых строк вместо отдельных ячеек

    def load_data(self):
        try:

            respondents = self.respondent_service.get_respondents()
            self.table.setRowCount(len(respondents))

            for row, respondent in enumerate(respondents):
                # Колонка ID (с числовой сортировкой)
                item_id = QTableWidgetItem()
                item_id.setData(Qt.DisplayRole, int(respondent.id))
                self.table.setItem(row, 0, item_id)

                self.table.setItem(row, 1, QTableWidgetItem(respondent.first_name))
                self.table.setItem(row, 2, QTableWidgetItem(respondent.last_name))
                self.table.setItem(row, 3, QTableWidgetItem(respondent.email))
                self.table.setItem(row, 4, QTableWidgetItem(respondent.gender))
                self.table.setItem(row, 5, QTableWidgetItem(respondent.country))
                age = QTableWidgetItem()
                age.setData(Qt.DisplayRole, int(respondent.age))
                self.table.setItem(row, 6, age)


        except Exception as e:
            QMessageBox.critical(self,
                                 "Ошибка загрузки",
                                 f"Не удалось загрузить данные: \n{str(e)}")

    def add_respondent(self, data: dict):
        self.respondent_service.add_respondent(
            data["first_name"],
            data["last_name"],
            data["email"],
            data["gender"],
            data["country"],
            data["age"]
        )
        self.load_data()
