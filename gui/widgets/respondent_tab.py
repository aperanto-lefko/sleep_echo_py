from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHeaderView, QTableWidget
from PySide6.QtCore import Qt
from exception.exceptions import RespondentNotFoundException


def create_int_item(value):
    item = QTableWidgetItem()
    item.setData(Qt.DisplayRole, value)
    return item


class RespondentsTab(QWidget):
    def __init__(self, ui, respondent_service):
        super().__init__()
        self.ui = ui
        self.respondent_service = respondent_service
        self.setup_table()
        self.connect_signals()

    def setup_table(self):
        self.ui.resp_tablewidget.setColumnCount(7)
        self.ui.resp_tablewidget.setHorizontalHeaderLabels([
            "ID", "First Name", "Last Name", "Email", "Gender", "Country", "Age"
        ])
        self.ui.resp_tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.resp_tablewidget.setSelectionBehavior(QTableWidget.SelectRows)
        

    def connect_signals(self):
        self.ui.all_respondents_btn.clicked.connect(self.load_all)
        self.ui.add_resp_btn.clicked.connect(self.add_respondent)
        self.ui.update_resp_btn.clicked.connect(self.update_respondent)
        self.ui.delete_resp_btn.clicked.connect(self.delete_respondent)
        self.ui.search_resp_btn.clicked.connect(self.search_by_last_name)
        self.ui.search_resp_by_id_btn.clicked.connect(self.search_by_id)

    def load_all(self):
        respondents = self.respondent_service.get_respondents()
        self.load_table(respondents)

    def load_table(self, respondents):
        self.ui.resp_tablewidget.setRowCount(0)
        self.ui.resp_tablewidget.setRowCount(len(respondents))
        for row, r in enumerate(respondents):
            self.ui.resp_tablewidget.setItem(row, 0, create_int_item(r.id))
            self.ui.resp_tablewidget.setItem(row, 1, QTableWidgetItem(r.first_name))
            self.ui.resp_tablewidget.setItem(row, 2, QTableWidgetItem(r.last_name))
            self.ui.resp_tablewidget.setItem(row, 3, QTableWidgetItem(r.email))
            self.ui.resp_tablewidget.setItem(row, 4, QTableWidgetItem(r.gender))
            self.ui.resp_tablewidget.setItem(row, 5, QTableWidgetItem(r.country))
            self.ui.resp_tablewidget.setItem(row, 6, create_int_item(r.age))
        self.ui.resp_tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.resp_tablewidget.setSortingEnabled(True)
        self.ui.resp_tablewidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.resp_tablewidget.setEditTriggers(QTableWidget.NoEditTriggers) #запрет редактирования
    def add_respondent(self):
        data = self.get_form_data()
        if not data: return
        self.respondent_service.add_respondent(**data)
        self.load_all()
        QMessageBox.information(self, "Успех", "Респондент добавлен")

    def update_respondent(self):
        try:
            data = self.get_form_data()
            if not data: return
            resp_id = int(self.ui.id_resp_search.text())
            self.respondent_service.update_respondent(resp_id, **data)
            self.load_all()
            QMessageBox.information(self, "Успех", "Респондент обновлён")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def delete_respondent(self):
        try:
            resp_id = int(self.ui.id_resp_delete.text())
            if self.respondent_service.delete_resp_by_id(resp_id):
                QMessageBox.information(self, "Успех", "Респондент удалён")
                self.load_all()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def search_by_last_name(self):
        last_name = self.ui.last_name_field_search.text()
        if not last_name:
            QMessageBox.warning(self, "Ошибка", "Введите фамилию")
            return
        respondents = self.respondent_service.search_resp_by_last_name(last_name)
        self.load_table(respondents)

    def search_by_id(self):
        try:
            resp_id = int(self.ui.id_resp_search.text())
            r = self.respondent_service.search_resp_by_id(resp_id)
            self.ui.name_resp.setText(r.first_name)
            self.ui.last_name_resp.setText(r.last_name)
            self.ui.email_resp.setText(r.email)
            self.ui.gender_box.setCurrentText(r.gender)
            self.ui.country_resp.setText(r.country)
            self.ui.age_resp.setText(str(r.age))
        except RespondentNotFoundException as e:
            QMessageBox.critical(self, "Ошибка", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def get_form_data(self):
        first_name = self.ui.name_resp.text()
        last_name = self.ui.last_name_resp.text()
        email = self.ui.email_resp.text()
        gender = self.ui.gender_box.currentText()
        country = self.ui.country_resp.text()
        age_text = self.ui.age_resp.text()

        if not (first_name and last_name and email and age_text.isdigit()):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля корректно")
            return None

        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "gender": gender,
            "country": country,
            "age": int(age_text),
        }
