from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView, QTableWidget
from PySide6.QtCore import Qt

from config.database_config import get_session
from exception.exceptions import RespondentNotFoundException
from repositories.respondent_repository import RespondentRepository
from services.respondent_service import RespondentService
from gui.ui_sleepecho_gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Sleepecho")

        session = next(get_session())
        self.respondent_service = RespondentService(RespondentRepository(session))

        self.initialize_table()

        self.ui.all_respondents_btn.clicked.connect(self.load_all_respondents)
        self.ui.add_resp_btn.clicked.connect(self.add_respondent)
        self.ui.search_resp_btn.clicked.connect(self.search_resp_by_last_name)
        self.ui.search_resp_by_id_btn.clicked.connect(self.search_resp_by_id)
        self.ui.update_resp_btn.clicked.connect(self.update_resp)
        self.ui.delete_resp_btn.clicked.connect(self.delete_resp)

    def initialize_table(self):
        self.ui.resp_tablewidget.setColumnCount(7)
        self.ui.resp_tablewidget.setHorizontalHeaderLabels([
            "ID", "First Name", "Last Name", "Email", "Gender", "Country", "Age"
        ])
        self.ui.resp_tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.resp_tablewidget.setSortingEnabled(True)
        self.ui.resp_tablewidget.setSelectionBehavior(QTableWidget.SelectRows)

    def load_all_respondents(self):
        try:
            respondents = self.respondent_service.get_respondents()
            self.load_data(respondents)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить респондентов:\n{str(e)}")

    def load_data(self, respondents):
        self.ui.resp_tablewidget.setRowCount(0)
        self.ui.resp_tablewidget.clearContents()
        self.ui.resp_tablewidget.setRowCount(len(respondents))

        for row, respondent in enumerate(respondents):
            item_id = QTableWidgetItem()
            item_id.setData(Qt.DisplayRole, int(respondent.id))
            self.ui.resp_tablewidget.setItem(row, 0, item_id)

            self.ui.resp_tablewidget.setItem(row, 1, QTableWidgetItem(respondent.first_name))
            self.ui.resp_tablewidget.setItem(row, 2, QTableWidgetItem(respondent.last_name))
            self.ui.resp_tablewidget.setItem(row, 3, QTableWidgetItem(respondent.email))
            self.ui.resp_tablewidget.setItem(row, 4, QTableWidgetItem(respondent.gender))
            self.ui.resp_tablewidget.setItem(row, 5, QTableWidgetItem(respondent.country))

            age_item = QTableWidgetItem()
            age_item.setData(Qt.DisplayRole, int(respondent.age))
            self.ui.resp_tablewidget.setItem(row, 6, age_item)

    def add_respondent(self):
        try:
            data = self.get_respondent_form_data()
            if data is None:
                return
            self.respondent_service.add_respondent(**data)
            self.load_all_respondents()

            self.ui.name_resp.clear()
            self.ui.last_name_resp.clear()
            self.ui.email_resp.clear()
            self.ui.gender_box.setCurrentIndex(0)
            self.ui.country_resp.clear()
            self.ui.age_resp.clear()

            QMessageBox.information(self, "Успех", "Респондент успешно добавлен")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить респондента:\n{str(e)}")

    def update_resp(self):
        try:
            data = self.get_respondent_form_data()
            if data is None:
                return
            resp_id = int(self.ui.id_resp_search.text())
            respondent = self.respondent_service.update_respondent(resp_id, **data)
            if respondent:
                self.load_all_respondents()
                QMessageBox.information(self, "Успех", "Респондент успешно обновлён")
            self.load_all_respondents()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось обновить респондента:\n{str(e)}")

    def search_resp_by_last_name(self):
        try:
            last_name = self.ui.last_name_field_search.text()
            if not last_name:
                QMessageBox.warning(self, "Ошибка", "Заполните поле \"Фамилия\" корректно")
                return
            respondents = self.respondent_service.search_resp_by_last_name(last_name)
            self.load_data(respondents)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось найти респондента:\n{str(e)}")

    def search_resp_by_id(self):
        try:
            resp_id_text = self.ui.id_resp_search.text()
            if not resp_id_text:
                QMessageBox.warning(self, "Ошибка", "Заполните поле \"id\" корректно")
                return
            resp_id = int(resp_id_text)
            respondent = self.respondent_service.search_resp_by_id(resp_id)

            self.ui.name_resp.setText(respondent.first_name)
            self.ui.last_name_resp.setText(respondent.last_name)
            self.ui.email_resp.setText(respondent.email)
            self.set_gender(respondent.gender)
            self.ui.age_resp.setText(str(respondent.age))
            self.ui.country_resp.setText(respondent.country)
        except RespondentNotFoundException as e:
            QMessageBox.critical(self, "Ошибка", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось найти респондента:\n{str(e)}")

    def delete_resp(self):
        try:
            resp_id_text = self.ui.id_resp_delete.text()
            if not resp_id_text:
                QMessageBox.warning(self, "Ошибка", "Заполните поле \"id\" корректно")
                return
            resp_id = int(resp_id_text)
            result = self.respondent_service.delete_resp_by_id(resp_id)
            if result:
               QMessageBox.information(self, "Успех", "Респондент успешно удален")
            self.load_all_respondents()
        except RespondentNotFoundException as e:
            QMessageBox.critical(self, "Ошибка", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось найти респондента:\n{str(e)}")
    def get_respondent_form_data(self):
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
            "age": int(age_text)
        }

    def set_gender(self, gender):
        if gender == "Male":
            self.ui.gender_box.setCurrentText("Male")
        elif gender == "Female":
            self.ui.gender_box.setCurrentText("Female")
        else:
            self.ui.gender_box.setCurrentText(" ")