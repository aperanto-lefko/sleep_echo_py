from PySide6.QtWidgets import QMainWindow
from gui.ui_sleepecho_gui import Ui_MainWindow
from gui.widgets.data_tab import SleepDataTab
from repositories.respondent_repository import RespondentRepository
from repositories.sleep_data_repository import SleepDataRepository
from services.respondent_service import RespondentService

from gui.widgets.respondent_tab import RespondentsTab
from config.database_config import get_session
from services.sleep_data_service import SleepDataService


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Sleepecho")

        session = next(get_session())

        respondent_service = RespondentService(RespondentRepository(session))
        data_service = SleepDataService(SleepDataRepository(session), respondent_service)
        # подключаем таб вкладки
        self.respondents_tab = RespondentsTab(self.ui, respondent_service)
        self.data_tab=SleepDataTab(self.ui,data_service)