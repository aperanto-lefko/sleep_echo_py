from PySide6.QtWidgets import QMainWindow
from gui.ui_sleepecho_gui import Ui_MainWindow
from repositories.respondent_repository import RespondentRepository
from services.respondent_service import RespondentService
from gui.widgets.respondent_tab import RespondentsTab
from config.database_config import get_session

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Sleepecho")

        session = next(get_session())
        respondent_service = RespondentService(RespondentRepository(session))

        # подключаем таб вкладки
        self.respondents_tab = RespondentsTab(self.ui, respondent_service)