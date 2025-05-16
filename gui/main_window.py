# Главное окно (логика + UI)
from PySide6.QtWidgets import QMainWindow, QMessageBox

from config.database_config import get_session
from gui.widgets.respondent_table import RespondentTable
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
        respondent_service = RespondentService(RespondentRepository(session))

        self.respondent_table = RespondentTable(self.ui.resp_tablewidget, respondent_service)

         #Обработчик на загрузку всех пользователей
        self.ui.all_respondents_btn.clicked.connect(
           self.respondent_table.load_data)

        self.ui.add_resp_btn.clicked.connect(self.add_respondent)

    def add_respondent(self):
            try:
                first_name = self.ui.name_resp.text()
                last_name = self.ui.last_name_resp.text()
                email = self.ui.email_resp.text()
                gender = self.ui.gender_box.currentText()
                country = self.ui.country_resp.text()
                age_text = self.ui.age_resp.text()

                if not (first_name and last_name and email and age_text.isdigit()):
                    QMessageBox.warning(self, "Ошибка", "Заполните все поля корректно")
                    return
                age = int(age_text)

                self.respondent_table.add_respondent( {
                    "first_name": first_name,
                    "last_name":last_name,
                    "email":email,
                    "gender":gender,
                    "country":country,
                    "age":age
                })

                self.ui.name_resp.clear()
                self.ui.last_name_resp.clear()
                self.ui.email_resp.clear()
                self.ui.gender_box.setCurrentIndex(0)
                self.ui.country_resp.clear()
                self.ui.age_resp.clear()

                QMessageBox.information(self, "Успех", "Респондент успешно добавлен")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось добавить респондента:\n{str(e)}")

