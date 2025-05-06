# Главное окно (логика + UI)
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from config.database_config import get_session
from gui.widgets.respondent_table import RespondentTable
from repositories.respondent_repository import RespondentRepository
from services.respondent_service import RespondentService


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Respondent Manager")

        session=next(get_session())
        respondent_service = RespondentService(RespondentRepository(session))

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.respondent_table = RespondentTable(respondent_service)
        layout.addWidget(self.respondent_table)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
