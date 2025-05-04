import sys

from config.database_config import get_session
from config.logging_config import setup_logging
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
    main()