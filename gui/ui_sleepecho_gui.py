# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sleepecho_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1251, 758)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(45, 45, 45);\n"
"	}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 542))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(45, 45, 45, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(45, 45, 45);\n"
"	}\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444444; /* \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0432\u043a\u043b\u0430\u0434\u043e\u043a */\n"
"    background: #222222;       /* \u0444\u043e\u043d \u043f\u0430\u043d\u0435\u043b\u0438 \u0432\u043a\u043b\u0430\u0434\u043e\u043a */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: rgb(62, 62, 62);;        /* \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043d\u0435\u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u0432\u043a\u043b\u0430\u0434\u043e\u043a */\n"
"    color: white;               /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 8px 16px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    border: 1px solid #444444;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(74, 144, 226);        /* \u0446\u0432\u0435"
                        "\u0442 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"    color: white;\n"
"    border: 1px solid #007ACC;\n"
"    border-bottom-color: #222222; /* \u0447\u0442\u043e\u0431\u044b \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u0430\u044f \u0432\u043a\u043b\u0430\u0434\u043a\u0430 \u0432\u0438\u0437\u0443\u0430\u043b\u044c\u043d\u043e \u0441\u043e\u0435\u0434\u0438\u043d\u044f\u043b\u0430\u0441\u044c \u0441 \u043f\u0430\u043d\u0435\u043b\u044c\u044e */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #005A9E;        /* \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        self.Resp_widget = QWidget()
        self.Resp_widget.setObjectName(u"Resp_widget")
        self.Resp_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(45, 45, 45);\n"
"	}\n"
"QPushButton {\n"
"    background-color: rgb(74, 144, 226);  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: 1px solid #555555;               /*  \u0440\u0430\u043c\u043a\u0430 */\n"
"    padding: 6px 12px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u043a\u0440\u0430\u0441\u043e\u0442\u044b */\n"
"    border-radius: 4px;         /* \u0421\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(60, 118, 184);  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 *"
                        "/\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(83, 163, 255);  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"QLabel {\n"
"    color: white;  /* \u0411\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgb(62, 62, 62);  /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 1px solid #555555;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 4px;\n"
"    border-radius: 3px;\n"
"}\n"
"QTableWidget {\n"
"    color: white;  /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043e \u0432\u0441\u0435\u0445 \u044f\u0447\u0435\u0439\u043a\u0430\u0445 */\n"
"    background-color:rgb(62, 62, 62);  /* \u0444\u043e\u043d \u0442\u0430\u0431\u043b\u0438\u0446\u044b (\u043e\u043f"
                        "\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e) */\n"
"}\n"
"QComboBox {\n"
"    background-color:rgb(62, 62, 62);   /* \u0444\u043e\u043d \u043f\u043e\u043b\u044f */\n"
"    color: white;                /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: 1px solid #555555;   /* \u0440\u0430\u043c\u043a\u0430 */\n"
"    padding: 4px 20px 4px 8px;   /* \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    border-radius: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(62, 62, 62); /* \u0444\u043e\u043d \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    color: white;              /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 */\n"
"    border: 1px solid #555555;\n"
"    selection-background-color: #007ACC; /* \u0446\u0432\u0435\u0442 \u043f\u043e\u0434\u0441\u0432\u0435\u0442\u043a\u0438 \u0432\u044b\u0431\u0440\u0430\u043d"
                        "\u043d\u043e\u0433\u043e */\n"
"    selection-color: white;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color:rgb(62, 62, 62); /* \u0444\u043e\u043d \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 */\n"
"    color: white;               /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 */\n"
"    padding: 4px;\n"
"    border: 1px solid #555555;\n"
"}\n"
"QHeaderView:horizontal::section {\n"
"    background-color: rgb(62, 62, 62);\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView:vertical::section {\n"
"    background-color: rgb(62, 62, 62);\n"
"    color: white;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Resp_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setContentsMargins(0, -1, -1, -1)
        self.label_7 = QLabel(self.Resp_widget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 3, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.resp_tablewidget = QTableWidget(self.Resp_widget)
        self.resp_tablewidget.setObjectName(u"resp_tablewidget")

        self.gridLayout_5.addWidget(self.resp_tablewidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 2, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.delete_resp_btn = QPushButton(self.Resp_widget)
        self.delete_resp_btn.setObjectName(u"delete_resp_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(30)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.delete_resp_btn.sizePolicy().hasHeightForWidth())
        self.delete_resp_btn.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.delete_resp_btn, 6, 1, 1, 1)

        self.label_11 = QLabel(self.Resp_widget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_11, 2, 1, 1, 1)

        self.search_resp_by_id_btn = QPushButton(self.Resp_widget)
        self.search_resp_by_id_btn.setObjectName(u"search_resp_by_id_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_resp_by_id_btn.sizePolicy().hasHeightForWidth())
        self.search_resp_by_id_btn.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.search_resp_by_id_btn, 1, 2, 1, 1)

        self.label_10 = QLabel(self.Resp_widget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_13 = QLabel(self.Resp_widget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(30)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.label_13, 5, 0, 1, 1)

        self.id_resp_search = QLineEdit(self.Resp_widget)
        self.id_resp_search.setObjectName(u"id_resp_search")
        sizePolicy2.setHeightForWidth(self.id_resp_search.sizePolicy().hasHeightForWidth())
        self.id_resp_search.setSizePolicy(sizePolicy2)
        self.id_resp_search.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.id_resp_search, 1, 1, 1, 1)

        self.label_12 = QLabel(self.Resp_widget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(30)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 4, 1, 1, 1)

        self.update_resp_btn = QPushButton(self.Resp_widget)
        self.update_resp_btn.setObjectName(u"update_resp_btn")
        sizePolicy2.setHeightForWidth(self.update_resp_btn.sizePolicy().hasHeightForWidth())
        self.update_resp_btn.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.update_resp_btn, 3, 1, 1, 1)

        self.id_resp_delete = QLineEdit(self.Resp_widget)
        self.id_resp_delete.setObjectName(u"id_resp_delete")
        sizePolicy2.setHeightForWidth(self.id_resp_delete.sizePolicy().hasHeightForWidth())
        self.id_resp_delete.setSizePolicy(sizePolicy2)
        self.id_resp_delete.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.id_resp_delete, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 4, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_9 = QLabel(self.Resp_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 3, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.email_resp = QLineEdit(self.Resp_widget)
        self.email_resp.setObjectName(u"email_resp")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(60)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.email_resp.sizePolicy().hasHeightForWidth())
        self.email_resp.setSizePolicy(sizePolicy6)
        self.email_resp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.email_resp, 2, 0, 1, 1)

        self.name_resp = QLineEdit(self.Resp_widget)
        self.name_resp.setObjectName(u"name_resp")
        sizePolicy6.setHeightForWidth(self.name_resp.sizePolicy().hasHeightForWidth())
        self.name_resp.setSizePolicy(sizePolicy6)
        self.name_resp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.name_resp, 0, 0, 1, 1)

        self.gender_label = QLabel(self.Resp_widget)
        self.gender_label.setObjectName(u"gender_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(60)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.gender_label.sizePolicy().hasHeightForWidth())
        self.gender_label.setSizePolicy(sizePolicy7)
        self.gender_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gender_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.gender_label, 3, 1, 1, 1)

        self.age_resp = QLineEdit(self.Resp_widget)
        self.age_resp.setObjectName(u"age_resp")
        sizePolicy6.setHeightForWidth(self.age_resp.sizePolicy().hasHeightForWidth())
        self.age_resp.setSizePolicy(sizePolicy6)
        self.age_resp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.age_resp, 4, 0, 1, 1)

        self.email_label = QLabel(self.Resp_widget)
        self.email_label.setObjectName(u"email_label")
        sizePolicy7.setHeightForWidth(self.email_label.sizePolicy().hasHeightForWidth())
        self.email_label.setSizePolicy(sizePolicy7)
        self.email_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.email_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.email_label, 2, 1, 1, 1)

        self.last_name_resp = QLineEdit(self.Resp_widget)
        self.last_name_resp.setObjectName(u"last_name_resp")
        sizePolicy6.setHeightForWidth(self.last_name_resp.sizePolicy().hasHeightForWidth())
        self.last_name_resp.setSizePolicy(sizePolicy6)
        self.last_name_resp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.last_name_resp, 1, 0, 1, 1)

        self.country_resp = QLineEdit(self.Resp_widget)
        self.country_resp.setObjectName(u"country_resp")
        sizePolicy6.setHeightForWidth(self.country_resp.sizePolicy().hasHeightForWidth())
        self.country_resp.setSizePolicy(sizePolicy6)
        self.country_resp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.country_resp, 5, 0, 1, 1)

        self.last_name_label = QLabel(self.Resp_widget)
        self.last_name_label.setObjectName(u"last_name_label")
        sizePolicy7.setHeightForWidth(self.last_name_label.sizePolicy().hasHeightForWidth())
        self.last_name_label.setSizePolicy(sizePolicy7)
        self.last_name_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.last_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.last_name_label, 1, 1, 1, 1)

        self.age_label = QLabel(self.Resp_widget)
        self.age_label.setObjectName(u"age_label")
        sizePolicy7.setHeightForWidth(self.age_label.sizePolicy().hasHeightForWidth())
        self.age_label.setSizePolicy(sizePolicy7)
        self.age_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.age_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.age_label, 4, 1, 1, 1)

        self.name_label = QLabel(self.Resp_widget)
        self.name_label.setObjectName(u"name_label")
        sizePolicy7.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy7)
        self.name_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.name_label, 0, 1, 1, 1)

        self.gender_box = QComboBox(self.Resp_widget)
        self.gender_box.addItem("")
        self.gender_box.addItem("")
        self.gender_box.addItem("")
        self.gender_box.setObjectName(u"gender_box")
        sizePolicy6.setHeightForWidth(self.gender_box.sizePolicy().hasHeightForWidth())
        self.gender_box.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.gender_box, 3, 0, 1, 1)

        self.country_label = QLabel(self.Resp_widget)
        self.country_label.setObjectName(u"country_label")
        sizePolicy7.setHeightForWidth(self.country_label.sizePolicy().hasHeightForWidth())
        self.country_label.setSizePolicy(sizePolicy7)
        self.country_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.country_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.country_label, 5, 1, 1, 1)

        self.add_resp_btn = QPushButton(self.Resp_widget)
        self.add_resp_btn.setObjectName(u"add_resp_btn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.add_resp_btn.sizePolicy().hasHeightForWidth())
        self.add_resp_btn.setSizePolicy(sizePolicy8)
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 0, 127, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        brush3 = QBrush(QColor(74, 144, 226, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush4)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush4)
        brush5 = QBrush(QColor(127, 127, 127, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush5)
        brush6 = QBrush(QColor(170, 170, 170, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 127))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush8)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush4)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush6)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush8)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush4)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush6)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
        brush9 = QBrush(QColor(127, 127, 127, 127))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush9)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush4)
#endif
        self.add_resp_btn.setPalette(palette1)

        self.gridLayout_4.addWidget(self.add_resp_btn, 0, 2, 6, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 4, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.last_name_field_search = QLineEdit(self.Resp_widget)
        self.last_name_field_search.setObjectName(u"last_name_field_search")
        sizePolicy1.setHeightForWidth(self.last_name_field_search.sizePolicy().hasHeightForWidth())
        self.last_name_field_search.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.last_name_field_search, 0, 4, 1, 1)

        self.label_8 = QLabel(self.Resp_widget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.label_8, 0, 3, 1, 1)

        self.search_resp_btn = QPushButton(self.Resp_widget)
        self.search_resp_btn.setObjectName(u"search_resp_btn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.search_resp_btn.sizePolicy().hasHeightForWidth())
        self.search_resp_btn.setSizePolicy(sizePolicy9)

        self.gridLayout_7.addWidget(self.search_resp_btn, 0, 2, 1, 1)

        self.all_respondents_btn = QPushButton(self.Resp_widget)
        self.all_respondents_btn.setObjectName(u"all_respondents_btn")
        sizePolicy9.setHeightForWidth(self.all_respondents_btn.sizePolicy().hasHeightForWidth())
        self.all_respondents_btn.setSizePolicy(sizePolicy9)

        self.gridLayout_7.addWidget(self.all_respondents_btn, 0, 0, 1, 1)

        self.widget = QWidget(self.Resp_widget)
        self.widget.setObjectName(u"widget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy10)

        self.gridLayout_7.addWidget(self.widget, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_7, 0, 0, 1, 2)

        self.tabWidget.addTab(self.Resp_widget, "")
        self.Data_widget = QWidget()
        self.Data_widget.setObjectName(u"Data_widget")
        self.Data_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(45, 45, 45);\n"
"	}\n"
"QPushButton {\n"
"    background-color: rgb(74, 144, 226);  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: 1px solid #555555;               /*  \u0440\u0430\u043c\u043a\u0430 */\n"
"    padding: 6px 12px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u043a\u0440\u0430\u0441\u043e\u0442\u044b */\n"
"    border-radius: 4px;         /* \u0421\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(60, 118, 184);  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 *"
                        "/\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(83, 163, 255);  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"QLabel {\n"
"    color: white;  /* \u0411\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgb(62, 62, 62);  /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 1px solid #555555;  /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 4px;\n"
"    border-radius: 3px;\n"
"}\n"
"QTableWidget {\n"
"    color: white;  /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043e \u0432\u0441\u0435\u0445 \u044f\u0447\u0435\u0439\u043a\u0430\u0445 */\n"
"    background-color:rgb(62, 62, 62);  /* \u0444\u043e\u043d \u0442\u0430\u0431\u043b\u0438\u0446\u044b (\u043e\u043f"
                        "\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e) */\n"
"}\n"
"QComboBox {\n"
"    background-color:rgb(62, 62, 62);   /* \u0444\u043e\u043d \u043f\u043e\u043b\u044f */\n"
"    color: white;                /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: 1px solid #555555;   /* \u0440\u0430\u043c\u043a\u0430 */\n"
"    padding: 4px 20px 4px 8px;   /* \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    border-radius: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(62, 62, 62); /* \u0444\u043e\u043d \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    color: white;              /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 */\n"
"    border: 1px solid #555555;\n"
"    selection-background-color: #007ACC; /* \u0446\u0432\u0435\u0442 \u043f\u043e\u0434\u0441\u0432\u0435\u0442\u043a\u0438 \u0432\u044b\u0431\u0440\u0430\u043d"
                        "\u043d\u043e\u0433\u043e */\n"
"    selection-color: white;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color:rgb(62, 62, 62); /* \u0444\u043e\u043d \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 */\n"
"    color: white;               /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 */\n"
"    padding: 4px;\n"
"    border: 1px solid #555555;\n"
"}\n"
"QHeaderView:horizontal::section {\n"
"    background-color: rgb(62, 62, 62);\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView:vertical::section {\n"
"    background-color: rgb(62, 62, 62);\n"
"    color: white;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.Data_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.coffee_end = QLineEdit(self.Data_widget)
        self.coffee_end.setObjectName(u"coffee_end")
        sizePolicy1.setHeightForWidth(self.coffee_end.sizePolicy().hasHeightForWidth())
        self.coffee_end.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.coffee_end, 2, 2, 1, 1)

        self.coffee_start = QLineEdit(self.Data_widget)
        self.coffee_start.setObjectName(u"coffee_start")
        sizePolicy1.setHeightForWidth(self.coffee_start.sizePolicy().hasHeightForWidth())
        self.coffee_start.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.coffee_start, 2, 1, 1, 1)

        self.exercise_end = QLineEdit(self.Data_widget)
        self.exercise_end.setObjectName(u"exercise_end")
        sizePolicy1.setHeightForWidth(self.exercise_end.sizePolicy().hasHeightForWidth())
        self.exercise_end.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.exercise_end, 1, 2, 1, 1)

        self.label_15 = QLabel(self.Data_widget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.label_15, 2, 0, 1, 1)

        self.exercise_start = QLineEdit(self.Data_widget)
        self.exercise_start.setObjectName(u"exercise_start")
        sizePolicy1.setHeightForWidth(self.exercise_start.sizePolicy().hasHeightForWidth())
        self.exercise_start.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.exercise_start, 1, 1, 1, 1)

        self.label_6 = QLabel(self.Data_widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.label_6, 0, 0, 1, 1)

        self.sl_quality_start = QLineEdit(self.Data_widget)
        self.sl_quality_start.setObjectName(u"sl_quality_start")
        sizePolicy1.setHeightForWidth(self.sl_quality_start.sizePolicy().hasHeightForWidth())
        self.sl_quality_start.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.sl_quality_start, 0, 1, 1, 1)

        self.label_14 = QLabel(self.Data_widget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.label_14, 1, 0, 1, 1)

        self.sl_quality_end = QLineEdit(self.Data_widget)
        self.sl_quality_end.setObjectName(u"sl_quality_end")
        sizePolicy1.setHeightForWidth(self.sl_quality_end.sizePolicy().hasHeightForWidth())
        self.sl_quality_end.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.sl_quality_end, 0, 2, 1, 1)

        self.label_16 = QLabel(self.Data_widget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.label_16, 3, 0, 1, 1)

        self.screen_time_start = QLineEdit(self.Data_widget)
        self.screen_time_start.setObjectName(u"screen_time_start")
        sizePolicy1.setHeightForWidth(self.screen_time_start.sizePolicy().hasHeightForWidth())
        self.screen_time_start.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.screen_time_start, 3, 1, 1, 1)

        self.screen_time_end = QLineEdit(self.Data_widget)
        self.screen_time_end.setObjectName(u"screen_time_end")
        sizePolicy1.setHeightForWidth(self.screen_time_end.sizePolicy().hasHeightForWidth())
        self.screen_time_end.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.screen_time_end, 3, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_16, 1, 1, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_2 = QWidget(self.Data_widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.Data_widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.widget_3, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_14, 4, 0, 1, 4)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.mood_start = QLineEdit(self.Data_widget)
        self.mood_start.setObjectName(u"mood_start")
        sizePolicy1.setHeightForWidth(self.mood_start.sizePolicy().hasHeightForWidth())
        self.mood_start.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.mood_start, 2, 1, 1, 1)

        self.work_time_start = QLineEdit(self.Data_widget)
        self.work_time_start.setObjectName(u"work_time_start")
        sizePolicy1.setHeightForWidth(self.work_time_start.sizePolicy().hasHeightForWidth())
        self.work_time_start.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.work_time_start, 0, 1, 1, 1)

        self.stress_end = QLineEdit(self.Data_widget)
        self.stress_end.setObjectName(u"stress_end")
        sizePolicy1.setHeightForWidth(self.stress_end.sizePolicy().hasHeightForWidth())
        self.stress_end.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.stress_end, 3, 2, 1, 1)

        self.label_19 = QLabel(self.Data_widget)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_20 = QLabel(self.Data_widget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.label_20, 3, 0, 1, 1)

        self.mood_end = QLineEdit(self.Data_widget)
        self.mood_end.setObjectName(u"mood_end")
        sizePolicy1.setHeightForWidth(self.mood_end.sizePolicy().hasHeightForWidth())
        self.mood_end.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.mood_end, 2, 2, 1, 1)

        self.stress_start = QLineEdit(self.Data_widget)
        self.stress_start.setObjectName(u"stress_start")
        sizePolicy1.setHeightForWidth(self.stress_start.sizePolicy().hasHeightForWidth())
        self.stress_start.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.stress_start, 3, 1, 1, 1)

        self.productivity_end = QLineEdit(self.Data_widget)
        self.productivity_end.setObjectName(u"productivity_end")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.productivity_end.sizePolicy().hasHeightForWidth())
        self.productivity_end.setSizePolicy(sizePolicy11)

        self.gridLayout_17.addWidget(self.productivity_end, 1, 2, 1, 1)

        self.productivity_start = QLineEdit(self.Data_widget)
        self.productivity_start.setObjectName(u"productivity_start")
        sizePolicy1.setHeightForWidth(self.productivity_start.sizePolicy().hasHeightForWidth())
        self.productivity_start.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.productivity_start, 1, 1, 1, 1)

        self.work_time_end = QLineEdit(self.Data_widget)
        self.work_time_end.setObjectName(u"work_time_end")
        sizePolicy1.setHeightForWidth(self.work_time_end.sizePolicy().hasHeightForWidth())
        self.work_time_end.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.work_time_end, 0, 2, 1, 1)

        self.label_18 = QLabel(self.Data_widget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.label_18, 1, 0, 1, 1)

        self.label_17 = QLabel(self.Data_widget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.label_17, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_17, 1, 3, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_4 = QLabel(self.Data_widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_11.addWidget(self.label_4, 2, 0, 1, 1)

        self.sl_end_time_end = QLineEdit(self.Data_widget)
        self.sl_end_time_end.setObjectName(u"sl_end_time_end")
        sizePolicy1.setHeightForWidth(self.sl_end_time_end.sizePolicy().hasHeightForWidth())
        self.sl_end_time_end.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.sl_end_time_end, 2, 2, 1, 1)

        self.sl_start_time_end = QLineEdit(self.Data_widget)
        self.sl_start_time_end.setObjectName(u"sl_start_time_end")
        sizePolicy1.setHeightForWidth(self.sl_start_time_end.sizePolicy().hasHeightForWidth())
        self.sl_start_time_end.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.sl_start_time_end, 1, 2, 1, 1)

        self.sl_end_time_start = QLineEdit(self.Data_widget)
        self.sl_end_time_start.setObjectName(u"sl_end_time_start")
        sizePolicy1.setHeightForWidth(self.sl_end_time_start.sizePolicy().hasHeightForWidth())
        self.sl_end_time_start.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.sl_end_time_start, 2, 1, 1, 1)

        self.label_2 = QLabel(self.Data_widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_11.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.Data_widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_11.addWidget(self.label_3, 1, 0, 1, 1)

        self.sl_start_time_start = QLineEdit(self.Data_widget)
        self.sl_start_time_start.setObjectName(u"sl_start_time_start")
        sizePolicy1.setHeightForWidth(self.sl_start_time_start.sizePolicy().hasHeightForWidth())
        self.sl_start_time_start.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.sl_start_time_start, 1, 1, 1, 1)

        self.search_id_resp = QLineEdit(self.Data_widget)
        self.search_id_resp.setObjectName(u"search_id_resp")
        sizePolicy1.setHeightForWidth(self.search_id_resp.sizePolicy().hasHeightForWidth())
        self.search_id_resp.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.search_id_resp, 0, 1, 1, 1)

        self.label_5 = QLabel(self.Data_widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_11.addWidget(self.label_5, 3, 0, 1, 1)

        self.sl_total_time_start = QLineEdit(self.Data_widget)
        self.sl_total_time_start.setObjectName(u"sl_total_time_start")
        sizePolicy1.setHeightForWidth(self.sl_total_time_start.sizePolicy().hasHeightForWidth())
        self.sl_total_time_start.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.sl_total_time_start, 3, 1, 1, 1)

        self.sl_total_time_end = QLineEdit(self.Data_widget)
        self.sl_total_time_end.setObjectName(u"sl_total_time_end")
        sizePolicy1.setHeightForWidth(self.sl_total_time_end.sizePolicy().hasHeightForWidth())
        self.sl_total_time_end.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.sl_total_time_end, 3, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_11, 1, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.delete_data_id = QLineEdit(self.Data_widget)
        self.delete_data_id.setObjectName(u"delete_data_id")
        sizePolicy1.setHeightForWidth(self.delete_data_id.sizePolicy().hasHeightForWidth())
        self.delete_data_id.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.delete_data_id, 5, 1, 1, 1)

        self.delete_data_btn = QPushButton(self.Data_widget)
        self.delete_data_btn.setObjectName(u"delete_data_btn")
        sizePolicy1.setHeightForWidth(self.delete_data_btn.sizePolicy().hasHeightForWidth())
        self.delete_data_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.delete_data_btn, 6, 1, 1, 1)

        self.update_data_id = QLineEdit(self.Data_widget)
        self.update_data_id.setObjectName(u"update_data_id")
        sizePolicy1.setHeightForWidth(self.update_data_id.sizePolicy().hasHeightForWidth())
        self.update_data_id.setSizePolicy(sizePolicy1)
        self.update_data_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.update_data_id, 1, 1, 1, 1)

        self.label_35 = QLabel(self.Data_widget)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_35, 1, 0, 1, 1)

        self.label_34 = QLabel(self.Data_widget)
        self.label_34.setObjectName(u"label_34")
        sizePolicy1.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy1)
        self.label_34.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_34.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_34.setLineWidth(-5)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.label_34, 0, 1, 1, 1)

        self.search_data_btn = QPushButton(self.Data_widget)
        self.search_data_btn.setObjectName(u"search_data_btn")
        sizePolicy1.setHeightForWidth(self.search_data_btn.sizePolicy().hasHeightForWidth())
        self.search_data_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.search_data_btn, 1, 2, 1, 1)

        self.label_36 = QLabel(self.Data_widget)
        self.label_36.setObjectName(u"label_36")
        sizePolicy1.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy1)
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_36, 2, 1, 1, 1)

        self.label_37 = QLabel(self.Data_widget)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_37, 4, 1, 1, 1)

        self.label_39 = QLabel(self.Data_widget)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_18.addWidget(self.label_39, 5, 0, 1, 1)

        self.update_data_btn = QPushButton(self.Data_widget)
        self.update_data_btn.setObjectName(u"update_data_btn")
        sizePolicy1.setHeightForWidth(self.update_data_btn.sizePolicy().hasHeightForWidth())
        self.update_data_btn.setSizePolicy(sizePolicy1)
        self.update_data_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_18.addWidget(self.update_data_btn, 3, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_18, 5, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.Data_widget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout_8.addLayout(self.horizontalLayout_2, 0, 0, 1, 4)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.sleep_quality = QLineEdit(self.Data_widget)
        self.sleep_quality.setObjectName(u"sleep_quality")
        sizePolicy1.setHeightForWidth(self.sleep_quality.sizePolicy().hasHeightForWidth())
        self.sleep_quality.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.sleep_quality, 4, 1, 1, 1)

        self.sleep_start_time = QLineEdit(self.Data_widget)
        self.sleep_start_time.setObjectName(u"sleep_start_time")
        sizePolicy1.setHeightForWidth(self.sleep_start_time.sizePolicy().hasHeightForWidth())
        self.sleep_start_time.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.sleep_start_time, 1, 1, 1, 1)

        self.update_id_resp = QLineEdit(self.Data_widget)
        self.update_id_resp.setObjectName(u"update_id_resp")
        sizePolicy1.setHeightForWidth(self.update_id_resp.sizePolicy().hasHeightForWidth())
        self.update_id_resp.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.update_id_resp, 0, 1, 1, 1)

        self.label_24 = QLabel(self.Data_widget)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_24, 1, 0, 1, 1)

        self.total_sleep_hours = QLineEdit(self.Data_widget)
        self.total_sleep_hours.setObjectName(u"total_sleep_hours")
        sizePolicy1.setHeightForWidth(self.total_sleep_hours.sizePolicy().hasHeightForWidth())
        self.total_sleep_hours.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.total_sleep_hours, 3, 1, 1, 1)

        self.label_27 = QLabel(self.Data_widget)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_27, 4, 0, 1, 1)

        self.label_22 = QLabel(self.Data_widget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_25 = QLabel(self.Data_widget)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_26 = QLabel(self.Data_widget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_26, 3, 0, 1, 1)

        self.sleep_end_time = QLineEdit(self.Data_widget)
        self.sleep_end_time.setObjectName(u"sleep_end_time")
        sizePolicy1.setHeightForWidth(self.sleep_end_time.sizePolicy().hasHeightForWidth())
        self.sleep_end_time.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.sleep_end_time, 2, 1, 1, 1)

        self.label_28 = QLabel(self.Data_widget)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_28, 5, 0, 1, 1)

        self.exercise_minutes = QLineEdit(self.Data_widget)
        self.exercise_minutes.setObjectName(u"exercise_minutes")
        sizePolicy1.setHeightForWidth(self.exercise_minutes.sizePolicy().hasHeightForWidth())
        self.exercise_minutes.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.exercise_minutes, 5, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_19, 5, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.productivity_score = QLineEdit(self.Data_widget)
        self.productivity_score.setObjectName(u"productivity_score")
        sizePolicy1.setHeightForWidth(self.productivity_score.sizePolicy().hasHeightForWidth())
        self.productivity_score.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.productivity_score, 3, 1, 1, 1)

        self.label_32 = QLabel(self.Data_widget)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.label_32, 4, 0, 1, 1)

        self.label_29 = QLabel(self.Data_widget)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.label_29, 1, 0, 1, 1)

        self.work_hours = QLineEdit(self.Data_widget)
        self.work_hours.setObjectName(u"work_hours")
        sizePolicy1.setHeightForWidth(self.work_hours.sizePolicy().hasHeightForWidth())
        self.work_hours.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.work_hours, 2, 1, 1, 1)

        self.label_23 = QLabel(self.Data_widget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.label_23, 0, 0, 1, 1)

        self.caffeine_intake_mg = QLineEdit(self.Data_widget)
        self.caffeine_intake_mg.setObjectName(u"caffeine_intake_mg")
        sizePolicy1.setHeightForWidth(self.caffeine_intake_mg.sizePolicy().hasHeightForWidth())
        self.caffeine_intake_mg.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.caffeine_intake_mg, 0, 1, 1, 1)

        self.mood_score = QLineEdit(self.Data_widget)
        self.mood_score.setObjectName(u"mood_score")
        sizePolicy1.setHeightForWidth(self.mood_score.sizePolicy().hasHeightForWidth())
        self.mood_score.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.mood_score, 4, 1, 1, 1)

        self.label_30 = QLabel(self.Data_widget)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.label_30, 2, 0, 1, 1)

        self.screen_time = QLineEdit(self.Data_widget)
        self.screen_time.setObjectName(u"screen_time")
        sizePolicy1.setHeightForWidth(self.screen_time.sizePolicy().hasHeightForWidth())
        self.screen_time.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.screen_time, 1, 1, 1, 1)

        self.label_31 = QLabel(self.Data_widget)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_33 = QLabel(self.Data_widget)
        self.label_33.setObjectName(u"label_33")
        sizePolicy1.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.label_33, 5, 0, 1, 1)

        self.stress_level = QLineEdit(self.Data_widget)
        self.stress_level.setObjectName(u"stress_level")
        sizePolicy1.setHeightForWidth(self.stress_level.sizePolicy().hasHeightForWidth())
        self.stress_level.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.stress_level, 5, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_12, 5, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.data_table_widget = QTableWidget(self.Data_widget)
        self.data_table_widget.setObjectName(u"data_table_widget")

        self.horizontalLayout.addWidget(self.data_table_widget)


        self.gridLayout_8.addLayout(self.horizontalLayout, 3, 0, 1, 4)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.all_data_btn = QPushButton(self.Data_widget)
        self.all_data_btn.setObjectName(u"all_data_btn")

        self.gridLayout_13.addWidget(self.all_data_btn, 0, 1, 1, 1)

        self.frame = QFrame(self.Data_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_13.addWidget(self.frame, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.Data_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.export_to_excel = QPushButton(self.widget_4)
        self.export_to_excel.setObjectName(u"export_to_excel")
        self.export_to_excel.setGeometry(QRect(100, 0, 251, 30))
        sizePolicy1.setHeightForWidth(self.export_to_excel.sizePolicy().hasHeightForWidth())
        self.export_to_excel.setSizePolicy(sizePolicy1)

        self.gridLayout_13.addWidget(self.widget_4, 0, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_13, 2, 0, 1, 4)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.create_data = QPushButton(self.Data_widget)
        self.create_data.setObjectName(u"create_data")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.create_data.sizePolicy().hasHeightForWidth())
        self.create_data.setSizePolicy(sizePolicy12)

        self.gridLayout_21.addWidget(self.create_data, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_21, 5, 2, 1, 1)

        self.tabWidget.addTab(self.Data_widget, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.all_respondents_btn, self.search_resp_btn)
        QWidget.setTabOrder(self.search_resp_btn, self.last_name_field_search)
        QWidget.setTabOrder(self.last_name_field_search, self.resp_tablewidget)
        QWidget.setTabOrder(self.resp_tablewidget, self.name_resp)
        QWidget.setTabOrder(self.name_resp, self.last_name_resp)
        QWidget.setTabOrder(self.last_name_resp, self.email_resp)
        QWidget.setTabOrder(self.email_resp, self.gender_box)
        QWidget.setTabOrder(self.gender_box, self.age_resp)
        QWidget.setTabOrder(self.age_resp, self.country_resp)
        QWidget.setTabOrder(self.country_resp, self.add_resp_btn)
        QWidget.setTabOrder(self.add_resp_btn, self.id_resp_search)
        QWidget.setTabOrder(self.id_resp_search, self.search_resp_by_id_btn)
        QWidget.setTabOrder(self.search_resp_by_id_btn, self.update_resp_btn)
        QWidget.setTabOrder(self.update_resp_btn, self.id_resp_delete)
        QWidget.setTabOrder(self.id_resp_delete, self.delete_resp_btn)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435/\u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0440\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u0430", None))
        self.delete_resp_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u043f\u043e\u043b\u044f \u0434\u043b\u044f \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.search_resp_by_id_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ID \u0440\u0435c\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u0430", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ID \u0440\u0435c\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u0430", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.update_resp_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0440\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u0430", None))
        self.gender_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.last_name_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.age_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.gender_box.setItemText(0, "")
        self.gender_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.gender_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.country_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.add_resp_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.search_resp_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0440\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.all_respondents_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435\u0445 \u0440\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Resp_widget), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0444\u0435\u0438\u043d, \u043c\u0433", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043d\u0430(1...10)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u0441\u043f\u043e\u0440\u0442\u0430, \u043c\u0438\u043d", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0443 \u044d\u043a\u0440\u0430\u043d\u0430, \u043c\u0438\u043d", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435(1...10)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0441\u0442\u0440\u0435\u0441\u0441\u0430(1...10)", None))
        self.work_time_end.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c(1...10)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0435\u0435 \u0432\u0440\u0435\u043c\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0431\u0443\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID \u0440\u0435c\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u0445\u043e\u0434\u0430 \u043a\u043e \u0441\u043d\u0443", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u0441\u043d\u0430", None))
        self.delete_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"ID \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.search_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u043f\u043e\u043b\u044f \u0434\u043b\u044f \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"ID \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.update_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u0445\u043e\u0434\u0430 \u043a\u043e \u0441\u043d\u0443", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043d\u0430(1...10)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"ID \u0440\u0435c\u043f\u043e\u043d\u0434\u0435\u043d\u0442\u0430", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0431\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u0441\u043d\u0430", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u0441\u043f\u043e\u0440\u0442\u0430, \u043c\u0438\u043d", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435(1...10)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0443 \u044d\u043a\u0440\u0430\u043d\u0430, \u043c\u0438\u043d", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0444\u0435\u0438\u043d, \u043c\u0433", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0435\u0435 \u0432\u0440\u0435\u043c\u044f", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c(1...10)", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0441\u0442\u0440\u0435\u0441\u0441\u0430(1...10)", None))
        self.all_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.export_to_excel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 EXCEL", None))
        self.create_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Data_widget), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

