# Настройки приложения
from dotenv import load_dotenv # это функция из библиотеки python-dotenv, которая загружает переменные из .env-файла в системные переменные окружения (os.environ).
import os #os — это стандартная библиотека Python для работы с операционной системой. os.getenv() — метод, который получает значение переменной окружения.

load_dotenv() #Загружает .env

class DbConfig:
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db_type = "postgresql"