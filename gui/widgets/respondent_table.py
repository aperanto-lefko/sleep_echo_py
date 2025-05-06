from PySide6.QtWidgets import QVBoxLayout, QTableWidget, QHBoxLayout, QLineEdit, QPushButton, QTableWidgetItem, QWidget


class RespondentTable(QWidget):
    def __init__(self, respondent_service):
        super().__init__()
        self.respondent_service = respondent_service

        self.layout = QVBoxLayout(self)

        # Таблица
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Форма добавления
        form_layout = QHBoxLayout()
        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText("first_name")
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("last_name")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("email")
        self.gender_input = QLineEdit()
        self.gender_input.setPlaceholderText("gender")
        self.country_input = QLineEdit()
        self.country_input.setPlaceholderText("country")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("age")
        self.add_button = QPushButton("Add Respondent")
        self.add_button.clicked.connect(self.add_respondent)

        form_layout.addWidget(self.first_name_input)
        form_layout.addWidget(self.last_name_input)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.gender_input)
        form_layout.addWidget(self.country_input)
        form_layout.addWidget(self.age_input)
        form_layout.addWidget(self.add_button)

        self.layout.addLayout(form_layout)

        self.load_data()

    def load_data(self):
        respondents = self.respondent_service.get_respondents()
        self.table.setRowCount(len(respondents))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "ID", "First Name", "Last Name", "Email", "Gender", "Country", "Age"
        ])

        for row, respondent in enumerate(respondents):
            self.table.setItem(row, 0, QTableWidgetItem(str(respondent.id)))
            self.table.setItem(row, 1, QTableWidgetItem(respondent.first_name))
            self.table.setItem(row, 2, QTableWidgetItem(respondent.last_name))
            self.table.setItem(row, 3, QTableWidgetItem(respondent.email))
            self.table.setItem(row, 4, QTableWidgetItem(respondent.gender))
            self.table.setItem(row, 5, QTableWidgetItem(respondent.country))
            self.table.setItem(row, 6, QTableWidgetItem(str(respondent.age)))

    def add_respondent(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        email = self.email_input.text()
        gender = self.gender_input.text()
        country = self.country_input.text()
        age_text = self.age_input.text()

        if first_name and last_name and email and age_text.isdigit():
            age = int(age_text)
            self.respondent_service.add_respondent(
                first_name=first_name,
                last_name=last_name,
                email=email,
                gender=gender,
                country=country,
                age=age
            )

            self.first_name_input.clear()
            self.last_name_input.clear()
            self.email_input.clear()
            self.gender_input.clear()
            self.country_input.clear()
            self.age_input.clear()

            self.load_data()