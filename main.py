import sys

from PySide6.QtWidgets import QApplication


from config.database_config import get_session, engine
from config.logging_config import setup_logging


from gui.main_window import MainWindow

setup_logging()
import logging
logger=logging.getLogger(__name__)

def main():
  logger.info("Запуск программы")
  try:
      with next(get_session()) as session:
          logger.info("Сессия успешно создана")
  except Exception as e:
      logger.error(f"Ошибка при выполнении main: {e}")

if __name__ =="__main__":
    #main()
    try:

        # Запуск приложения
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        logger.error(f"Ошибка при запуске приложения: {e}")
        sys.exit(1)