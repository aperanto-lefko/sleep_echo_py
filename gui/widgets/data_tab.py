import logging

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QMessageBox, QFileDialog
from sqlalchemy.exc import NoResultFound

from openpyxl import Workbook

logger = logging.getLogger(__name__)

def create_int_item(value):
    item = QTableWidgetItem()
    item.setData(Qt.DisplayRole, value)
    return item

def parse_int_or_null(text):
        return 0 if not text.strip() else int(text)

def parse_float_or_null(text):
    return 0.0 if not text.strip() else float(text)

class SleepDataTab(QWidget):
    def __init__(self, ui, sleep_data_service):
        super().__init__()
        self.ui = ui
        self.sleep_data_service = sleep_data_service
        self.setup_table()
        self.connect_signals()

    def setup_table(self):
        self.ui.data_table_widget.setColumnCount(14)
        self.ui.data_table_widget.setHorizontalHeaderLabels([
            "ID", "Date", "RespId", "sleepStartTime", "SleepEndTime", "TotalSleepHours", "SleepQuality", "ExerciseMinutes", "CaffeineIntakeMg", "ScreenTime",
            "WorkHours", "ProductivityScore", "MoodScore", "StressLevel"
        ])

        self.ui.data_table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        header = self.ui.data_table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)  # Позволяет изменять ширину
        header.setSectionsMovable(True)  # Разрешает перетаскивание столбцов

    def connect_signals(self):
        self.ui.all_data_btn.clicked.connect(self.load_all)
        self.ui.search_data_btn.clicked.connect(self.search_sleep_data_by_id_for_update)
        self.ui.update_data_btn.clicked.connect(self.date_update)
        self.ui.delete_data_btn.clicked.connect(self.delete_data)
        self.ui.export_to_excel.clicked.connect(self.export_data)
        self.ui.create_data.clicked.connect(self.create_data)

    def load_all(self):

        try:
            # Парсинг параметров из полей ввода
            respondent_id = parse_int_or_null(self.ui.search_id_resp.text())
            sl_start_time_start = parse_float_or_null(self.ui.sl_start_time_start.text())
            sl_start_time_end = parse_float_or_null(self.ui.sl_start_time_end.text())
            sl_end_time_start = parse_float_or_null(self.ui.sl_end_time_start.text())
            sl_end_time_end = parse_float_or_null(self.ui.sl_end_time_end.text())
            sl_total_time_start = parse_float_or_null(self.ui.sl_total_time_start.text())
            sl_total_time_end = parse_float_or_null(self.ui.sl_total_time_end.text())
            sl_quality_start = parse_int_or_null(self.ui.sl_quality_start.text())
            sl_quality_end = parse_int_or_null(self.ui.sl_quality_end.text())
            exercise_start = parse_int_or_null(self.ui.exercise_start.text())
            exercise_end = parse_int_or_null(self.ui.exercise_end.text())
            coffee_start = parse_int_or_null(self.ui.coffee_start.text())
            coffee_end = parse_int_or_null(self.ui.coffee_end.text())
            screen_time_start = parse_int_or_null(self.ui.screen_time_start.text())
            screen_time_end = parse_int_or_null(self.ui.screen_time_end.text())
            work_time_start = parse_float_or_null(self.ui.work_time_start.text())
            work_time_end = parse_float_or_null(self.ui.work_time_end.text())
            productivity_start = parse_int_or_null(self.ui.productivity_start.text())
            productivity_end = parse_int_or_null(self.ui.productivity_end.text())
            mood_start = parse_int_or_null(self.ui.mood_start.text())
            mood_end = parse_int_or_null(self.ui.mood_end.text())
            stress_start = parse_int_or_null(self.ui.stress_start.text())
            stress_end = parse_int_or_null(self.ui.stress_end.text())



            # Получение данных через сервис
            sleep_data = self.sleep_data_service.get_sleep_data_with_parameters(
                respondent_id,
                sl_start_time_start,
                sl_start_time_end,
                sl_end_time_start,
                sl_end_time_end,
                sl_total_time_start,
                sl_total_time_end,
                sl_quality_start,
                sl_quality_end,
                exercise_start,
                exercise_end,
                coffee_start,
                coffee_end,
                screen_time_start,
                screen_time_end,
                work_time_start,
                work_time_end,
                productivity_start,
                productivity_end,
                mood_start,
                mood_end,
                stress_start,
                stress_end
            )

            if not sleep_data:
                QMessageBox.information(self, "Информация", "Данные с такими параметрами не найдены")
                self.ui.data_table_widget.setRowCount(0)
            else:
                QMessageBox.information(self, "Успех", f"Загружено {len(sleep_data)} записей.")
                logger.info(f"Успешная загрузка данных. Загружено {len(sleep_data)} записей")
                self.load_table(sleep_data)

        except Exception as ex:
            error_msg = f"Непредвиденная ошибка: {str(ex)}"
            QMessageBox.critical(self, "Ошибка", error_msg)
            logger.error(error_msg)



    def load_table(self, sleep_data):
        self.ui.data_table_widget.setRowCount(0)
        self.ui.data_table_widget.setRowCount(len(sleep_data))
        for row, data in enumerate(sleep_data):
            # ID
            self.ui.data_table_widget.setItem(row, 0, create_int_item(data.id))

            date_str = data.sleep_date.strftime("%Y-%m-%d") if data.sleep_date else ""
            self.ui.data_table_widget.setItem(row, 1, QTableWidgetItem(date_str))

            self.ui.data_table_widget.setItem(row, 2, create_int_item(data.person_id))

            # Время начала сна (форматируем float)
            self.ui.data_table_widget.setItem(row, 3, QTableWidgetItem(f"{data.sleep_start_time:.2f}"))

            self.ui.data_table_widget.setItem(row, 4, QTableWidgetItem(f"{data.sleep_end_time:.2f}"))

            self.ui.data_table_widget.setItem(row, 5, QTableWidgetItem(f"{data.total_sleep_hours:.2f}"))

            self.ui.data_table_widget.setItem(row, 6, create_int_item(data.sleep_quality))

            self.ui.data_table_widget.setItem(row, 7, create_int_item(data.exercise_minutes))

            self.ui.data_table_widget.setItem(row, 8, create_int_item(data.caffeine_intake_mg))

            self.ui.data_table_widget.setItem(row, 9, create_int_item(data.screen_time_before_bed))

            self.ui.data_table_widget.setItem(row, 10, QTableWidgetItem(f"{data.work_hours:.2f}"))

            self.ui.data_table_widget.setItem(row, 11, create_int_item(data.productivity_score))

            self.ui.data_table_widget.setItem(row, 12, create_int_item(data.mood_score))

            self.ui.data_table_widget.setItem(row, 13, create_int_item(data.stress_level))

            # Настройки таблицы
        self.ui.data_table_widget.setSortingEnabled(True)
        self.ui.data_table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.data_table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

    def search_sleep_data_by_id_for_update(self):
        try:
            data_id = int(self.ui.update_data_id.text())
            sleep_data = self.sleep_data_service.get_sleep_data_by_id(data_id)
            self.ui.update_id_resp.setText(str(sleep_data.respondent.id))
            self.ui.sleep_start_time.setText(str(sleep_data.sleep_start_time))
            self.ui.sleep_end_time.setText(str(sleep_data.sleep_end_time))
            self.ui.total_sleep_hours.setText(str(sleep_data.total_sleep_hours))
            self.ui.sleep_quality.setText(str(sleep_data.sleep_quality))
            self.ui.exercise_minutes.setText(str(sleep_data.exercise_minutes))
            self.ui.caffeine_intake_mg.setText(str(sleep_data.caffeine_intake_mg))
            self.ui.screen_time.setText(str(sleep_data.screen_time_before_bed))
            self.ui.work_hours.setText(str(sleep_data.work_hours))
            self.ui.productivity_score.setText(str(sleep_data.productivity_score))
            self.ui.mood_score.setText(str(sleep_data.mood_score))
            self.ui.stress_level.setText(str(sleep_data.stress_level))
        except NoResultFound as ex:
            error_msg = f"Данные не найдены: {str(ex)}"
            QMessageBox.warning(self, "Ошибка", error_msg)
            logger.error(error_msg)

    def highlight_textbox(self, textbox):
        textbox.setStyleSheet("border: 2px solid red;")
        QMessageBox.warning(self, "Внимание", "Необходимо заполнить все поля")
        QTimer.singleShot(700, lambda: textbox.setStyleSheet(""))

    def date_update(self):
        try:
            if not self.ui.update_data_id.text().strip():
                self.highlight_textbox(self.ui.update_data_id)
                return

            data_id = int(self.ui.update_data_id.text())

            parsed_data = self.parse_input_data_fields()
            if parsed_data is None:
                return

            (respondent_id, sl_start_time, sl_end_time, sl_total_time,
             sl_quality, exercise, coffee, screen_time, work_time,
             productivity, mood, stress) = parsed_data

            msg = f"""Обновить данные с id {data_id} для респондента с id:{respondent_id}:
Время отхода ко сну: {sl_start_time},
Время пробуждения: {sl_end_time},
Общее время сна: {sl_total_time},
Качество сна: {sl_quality},
Время для спорта: {exercise},
Кофеин: {coffee},
Время у экрана: {screen_time},
Рабочее время: {work_time},
Производительность: {productivity},
Настроение: {mood},
Уровень стресса: {stress}?"""

            reply = QMessageBox.question(self, 'Обновление данных', msg,
                                         QMessageBox.Ok | QMessageBox.Cancel,
                                         QMessageBox.Cancel)

            if reply == QMessageBox.Ok:

                success = self.sleep_data_service.update_sleep_data(data_id,
                                                                    respondent_id,
                                                                    sl_start_time,
                                                                    sl_end_time,
                                                                    sl_total_time,
                                                                    sl_quality,
                                                                    exercise,
                                                                    coffee,
                                                                    screen_time,
                                                                    work_time,
                                                                    productivity,
                                                                    mood,
                                                                    stress)

                if success:
                    QMessageBox.information(self, "Успех",
                                            f"Данные для записи id={data_id} успешно обновлены")
                    logger.info(f"Успешное обновление записи {data_id}")
                else:
                    QMessageBox.warning(self, "Ошибка", "Данные не обновлены")
                    logger.info(f"Данные не обновлены {data_id}")

        except ValueError as ex:
            QMessageBox.critical(self, "Ошибка", f"Некорректные данные: {str(ex)}")
            logger.error(f"Ошибка валидации: {str(ex)}")
        except Exception as ex:
            QMessageBox.critical(self, "Ошибка", f"Непредвиденная ошибка: {str(ex)}")
            logger.error(f"Непредвиденная ошибка: {str(ex)}")

    def parse_input_data_fields(self):
        """Парсит и валидирует все входные поля, выделяет невалидные"""

        if not self.ui.update_id_resp.text().strip():
            self.highlight_textbox(self.ui.update_id_resp)
            return None
        try:
            respondent_id = int(self.ui.update_id_resp.text())
        except ValueError:
            self.highlight_textbox(self.ui.update_id_resp)
            return None


        if not self.ui.sleep_start_time.text().strip():
            self.highlight_textbox(self.ui.sleep_start_time)
            return None
        try:
            sl_start_time = float(self.ui.sleep_start_time.text())
        except ValueError:
            self.highlight_textbox(self.ui.sleep_start_time)
            return None


        if not self.ui.sleep_end_time.text().strip():
            self.highlight_textbox(self.ui.sleep_end_time)
            return None
        try:
            sl_end_time = float(self.ui.sleep_end_time.text())
        except ValueError:
            self.highlight_textbox(self.ui.sleep_end_time)
            return None


        if not self.ui.total_sleep_hours.text().strip():
            self.highlight_textbox(self.ui.total_sleep_hours)
            return None
        try:
            sl_total_time = float(self.ui.total_sleep_hours.text())
        except ValueError:
            self.highlight_textbox(self.ui.total_sleep_hours)
            return None


        if not self.ui.sleep_quality.text().strip():
            self.highlight_textbox(self.ui.sleep_quality)
            return None
        try:
            sl_quality = int(self.ui.sleep_quality.text())
        except ValueError:
            self.highlight_textbox(self.ui.sleep_quality)
            return None


        if not self.ui.exercise_minutes.text().strip():
            self.highlight_textbox(self.ui.exercise_minutes)
            return None
        try:
            exercise = int(self.ui.exercise_minutes.text())
        except ValueError:
            self.highlight_textbox(self.ui.exercise_minutes)
            return None


        if not self.ui.caffeine_intake_mg.text().strip():
            self.highlight_textbox(self.ui.caffeine_intake_mg)
            return None
        try:
            coffee = int(self.ui.caffeine_intake_mg.text())
        except ValueError:
            self.highlight_textbox(self.ui.caffeine_intake_mg)
            return None


        if not self.ui.screen_time.text().strip():
            self.highlight_textbox(self.ui.screen_time)
            return None
        try:
            screen_time = int(self.ui.screen_time.text())
        except ValueError:
            self.highlight_textbox(self.ui.screen_time)
            return None


        if not self.ui.work_hours.text().strip():
            self.highlight_textbox(self.ui.work_hours)
            return None
        try:
            work_time = float(self.ui.work_hours.text())
        except ValueError:
            self.highlight_textbox(self.ui.work_hours)
            return None


        if not self.ui.productivity_score.text().strip():
            self.highlight_textbox(self.ui.productivity_score)
            return None
        try:
            productivity = int(self.ui.productivity_score.text())
        except ValueError:
            self.highlight_textbox(self.ui.productivity_score)
            return None


        if not self.ui.mood_score.text().strip():
            self.highlight_textbox(self.ui.mood_score.text())
            return None
        try:
            mood = int(self.ui.mood_score.text())
        except ValueError:
            self.highlight_textbox(self.ui.mood_score.text())
            return None


        if not self.ui.stress_level.text().strip():
            self.highlight_textbox(self.ui.stress_level)
            return None
        try:
            stress = int(self.ui.stress_level.text())
        except ValueError:
            self.highlight_textbox(self.ui.stress_level)
            return None


        return (
            respondent_id,
            sl_start_time,
            sl_end_time,
            sl_total_time,
            sl_quality,
            exercise,
            coffee,
            screen_time,
            work_time,
            productivity,
            mood,
            stress
        )

    def delete_data(self):
        try:
            if not self.ui.delete_data_id.text().strip():
                self.highlight_textbox(self.ui.delete_data_id)
                return

            data_id = int(self.ui.delete_data_id.text())

            if self.sleep_data_service.remove_sleep_data_by_id(data_id):
                QMessageBox.information(self, "Успех",
                                        f"Данные с id={data_id} удалены")
                logger.info(f"Успешное удаление записи {data_id}")
            else:
                QMessageBox.warning(self, "Ошибка", "Данные не удалены")
                logger.warning(f"Не удалось удалить запись {data_id}")

        except ValueError:
            self.highlight_textbox(self.ui.deleted_data_id_textbox)
            QMessageBox.critical(self, "Ошибка",
                                 "Некорректный ID. Введите целое число.")
            logger.error("Некорректный формат ID для удаления")

        except NoResultFound as ex:
            QMessageBox.critical(self, "Ошибка", str(ex))
            logger.error(f"Данные не найдены: {str(ex)}")



        except Exception as ex:
            QMessageBox.critical(self, "Ошибка",
                                 f"Непредвиденная ошибка: {str(ex)}")
            logger.error(f"Непредвиденная ошибка при удалении: {str(ex)}")

    def export_data(self):
        """Экспорт данных из таблицы в Excel файл"""
        table_widget = self.ui.data_table_widget
        if table_widget.rowCount() == 0:
            QMessageBox.warning(self, "Предупреждение",
                                "Нет данных для экспорта.")
            return

        # Настройка диалога сохранения файла
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Экспорт в Excel")
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Excel Files (*.xlsx);;All Files (*)")
        file_dialog.setDefaultSuffix("xlsx")
        file_dialog.selectFile("Data.xlsx")  # Имя файла по умолчанию

        if file_dialog.exec() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            self.export_to_excel(table_widget, file_path)

    def export_to_excel(self, table_widget: QTableWidget, file_path: str):
        """Создание Excel файла с данными из таблицы"""
        try:
            # Создаем новую книгу Excel
            wb = Workbook()
            ws = wb.active
            ws.title = "Exported Data"

            # Добавляем заголовки столбцов
            headers = []
            for col in range(table_widget.columnCount()):
                header = table_widget.horizontalHeaderItem(col)
                headers.append(header.text() if header else f"Column {col + 1}")
            ws.append(headers)

            # Добавляем данные из таблицы
            for row in range(table_widget.rowCount()):
                row_data = []
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    row_data.append(item.text() if item else "")
                ws.append(row_data)

            # Сохраняем файл
            wb.save(file_path)

            # Показываем сообщение об успехе
            QMessageBox.information(
                self,
                "Экспорт завершен",
                f"Данные успешно экспортированы в:\n{file_path}"
            )

        except PermissionError:
            QMessageBox.critical(
                self,
                "Ошибка",
                "Нет прав для записи файла. Закройте файл если он открыт."
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Ошибка экспорта",
                f"Произошла ошибка при экспорте:\n{str(e)}"
            )

    def create_data(self):
        try:
            parsed_data = self.parse_input_data_fields()
            if parsed_data is None:
                return

            (respondent_id, sl_start_time, sl_end_time, sl_total_time,
             sl_quality, exercise, coffee, screen_time, work_time,
             productivity, mood, stress) = parsed_data


            new_sleep_data = self.sleep_data_service.add_sleep_data(
                respondent_id,
                sl_start_time,
                sl_end_time,
                sl_total_time,
                sl_quality,
                exercise,
                coffee,
                screen_time,
                work_time,
                productivity,
                mood,
                stress
            )

            if new_sleep_data is not None:
                QMessageBox.information(
                    self,
                    "Успех",
                    f"Добавлена запись {new_sleep_data}",
                    QMessageBox.Ok
                )
                logger.info(f"Успешное добавление новой записи {new_sleep_data.id}")

        except NoResultFound as ex:
            QMessageBox.critical(
                self,
                "Ошибка",
                str(ex),
                QMessageBox.Ok
            )
            logger.error(f"Данные не найдены: {str(ex)}")

        except Exception as ex:
            QMessageBox.critical(
                self,
                "Ошибка",
                f"Непредвиденная ошибка: {str(ex)}",
                QMessageBox.Ok
            )
            logger.error(f"Непредвиденная ошибка: {str(ex)}")