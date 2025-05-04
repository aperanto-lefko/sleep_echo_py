# Данные для подключения к PostgreSQL
import os

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import logging
logger = logging.getLogger(__name__)
# Загружаем переменные окружения из файла .env
load_dotenv()

def init_engine():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        logger.warning("DATABASE_URL не загружен")
        raise ValueError("DATABASE_URL не загружен из переменных окружения")

    try:
      engine=create_engine(database_url, echo=True)
      #Пробное подключение
      with engine.connect():
          logger.info("Успешное подключение к базе данных")
          return engine
    except SQLAlchemyError as e:
        logger.error(f"Ошибка подключения к базе данных: {e}")
        raise
    except Exception as e:
        logger.error(f"Непредвиденная ошибка: {e}")
        raise

engine = init_engine()

def get_session():
  try:
    with Session(engine) as session:
        yield session
  except SQLAlchemyError as e:
      logger.error(f"Ошибка создания сессии: {e}")
      raise



