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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 733)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        brush1 = QBrush(QColor(0, 85, 255, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setContentsMargins(0, -1, -1, -1)
        self.label_7 = QLabel(self.widget_2)
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
        self.table_resp = QTableView(self.widget_2)
        self.table_resp.setObjectName(u"table_resp")

        self.gridLayout_5.addWidget(self.table_resp, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 2, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.delete_resp_btn = QPushButton(self.widget_2)
        self.delete_resp_btn.setObjectName(u"delete_resp_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(30)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.delete_resp_btn.sizePolicy().hasHeightForWidth())
        self.delete_resp_btn.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.delete_resp_btn, 6, 1, 1, 1)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_11, 2, 1, 1, 1)

        self.search_resp_by_id_btn = QPushButton(self.widget_2)
        self.search_resp_by_id_btn.setObjectName(u"search_resp_by_id_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_resp_by_id_btn.sizePolicy().hasHeightForWidth())
        self.search_resp_by_id_btn.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.search_resp_by_id_btn, 1, 2, 1, 1)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(30)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.label_13, 5, 0, 1, 1)

        self.id_resp_search = QLineEdit(self.widget_2)
        self.id_resp_search.setObjectName(u"id_resp_search")
        sizePolicy2.setHeightForWidth(self.id_resp_search.sizePolicy().hasHeightForWidth())
        self.id_resp_search.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.id_resp_search, 1, 1, 1, 1)

        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(30)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 4, 1, 1, 1)

        self.update_resp_btn = QPushButton(self.widget_2)
        self.update_resp_btn.setObjectName(u"update_resp_btn")
        sizePolicy2.setHeightForWidth(self.update_resp_btn.sizePolicy().hasHeightForWidth())
        self.update_resp_btn.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.update_resp_btn, 3, 1, 1, 1)

        self.id_resp_delete = QLineEdit(self.widget_2)
        self.id_resp_delete.setObjectName(u"id_resp_delete")
        sizePolicy2.setHeightForWidth(self.id_resp_delete.sizePolicy().hasHeightForWidth())
        self.id_resp_delete.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.id_resp_delete, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 4, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 3, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.email_resp = QLineEdit(self.widget_2)
        self.email_resp.setObjectName(u"email_resp")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(60)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.email_resp.sizePolicy().hasHeightForWidth())
        self.email_resp.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.email_resp, 2, 0, 1, 1)

        self.name_resp = QLineEdit(self.widget_2)
        self.name_resp.setObjectName(u"name_resp")
        sizePolicy6.setHeightForWidth(self.name_resp.sizePolicy().hasHeightForWidth())
        self.name_resp.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.name_resp, 0, 0, 1, 1)

        self.gender_label = QLabel(self.widget_2)
        self.gender_label.setObjectName(u"gender_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(60)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.gender_label.sizePolicy().hasHeightForWidth())
        self.gender_label.setSizePolicy(sizePolicy7)
        self.gender_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gender_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.gender_label, 3, 1, 1, 1)

        self.age_resp = QLineEdit(self.widget_2)
        self.age_resp.setObjectName(u"age_resp")
        sizePolicy6.setHeightForWidth(self.age_resp.sizePolicy().hasHeightForWidth())
        self.age_resp.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.age_resp, 4, 0, 1, 1)

        self.email_label = QLabel(self.widget_2)
        self.email_label.setObjectName(u"email_label")
        sizePolicy7.setHeightForWidth(self.email_label.sizePolicy().hasHeightForWidth())
        self.email_label.setSizePolicy(sizePolicy7)
        self.email_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.email_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.email_label, 2, 1, 1, 1)

        self.last_name_resp = QLineEdit(self.widget_2)
        self.last_name_resp.setObjectName(u"last_name_resp")
        sizePolicy6.setHeightForWidth(self.last_name_resp.sizePolicy().hasHeightForWidth())
        self.last_name_resp.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.last_name_resp, 1, 0, 1, 1)

        self.country_resp = QLineEdit(self.widget_2)
        self.country_resp.setObjectName(u"country_resp")
        sizePolicy6.setHeightForWidth(self.country_resp.sizePolicy().hasHeightForWidth())
        self.country_resp.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.country_resp, 5, 0, 1, 1)

        self.last_name_label = QLabel(self.widget_2)
        self.last_name_label.setObjectName(u"last_name_label")
        sizePolicy7.setHeightForWidth(self.last_name_label.sizePolicy().hasHeightForWidth())
        self.last_name_label.setSizePolicy(sizePolicy7)
        self.last_name_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.last_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.last_name_label, 1, 1, 1, 1)

        self.age_label = QLabel(self.widget_2)
        self.age_label.setObjectName(u"age_label")
        sizePolicy7.setHeightForWidth(self.age_label.sizePolicy().hasHeightForWidth())
        self.age_label.setSizePolicy(sizePolicy7)
        self.age_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.age_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.age_label, 4, 1, 1, 1)

        self.name_label = QLabel(self.widget_2)
        self.name_label.setObjectName(u"name_label")
        sizePolicy7.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy7)
        self.name_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.name_label, 0, 1, 1, 1)

        self.gender_box = QComboBox(self.widget_2)
        self.gender_box.addItem("")
        self.gender_box.addItem("")
        self.gender_box.addItem("")
        self.gender_box.setObjectName(u"gender_box")
        sizePolicy6.setHeightForWidth(self.gender_box.sizePolicy().hasHeightForWidth())
        self.gender_box.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.gender_box, 3, 0, 1, 1)

        self.country_label = QLabel(self.widget_2)
        self.country_label.setObjectName(u"country_label")
        sizePolicy7.setHeightForWidth(self.country_label.sizePolicy().hasHeightForWidth())
        self.country_label.setSizePolicy(sizePolicy7)
        self.country_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.country_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.country_label, 5, 1, 1, 1)

        self.add_resp_btn = QPushButton(self.widget_2)
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
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        brush4 = QBrush(QColor(127, 127, 127, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(170, 170, 170, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush6)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush3)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush6)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush3)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush6)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
        brush8 = QBrush(QColor(127, 127, 127, 127))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush3)
#endif
        self.add_resp_btn.setPalette(palette1)

        self.gridLayout_4.addWidget(self.add_resp_btn, 0, 2, 6, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 4, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.last_name_field_search = QLineEdit(self.widget_2)
        self.last_name_field_search.setObjectName(u"last_name_field_search")
        sizePolicy1.setHeightForWidth(self.last_name_field_search.sizePolicy().hasHeightForWidth())
        self.last_name_field_search.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.last_name_field_search, 0, 4, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.label_8, 0, 3, 1, 1)

        self.search_resp_btn = QPushButton(self.widget_2)
        self.search_resp_btn.setObjectName(u"search_resp_btn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.search_resp_btn.sizePolicy().hasHeightForWidth())
        self.search_resp_btn.setSizePolicy(sizePolicy9)

        self.gridLayout_7.addWidget(self.search_resp_btn, 0, 2, 1, 1)

        self.all_respondents_btn = QPushButton(self.widget_2)
        self.all_respondents_btn.setObjectName(u"all_respondents_btn")
        sizePolicy9.setHeightForWidth(self.all_respondents_btn.sizePolicy().hasHeightForWidth())
        self.all_respondents_btn.setSizePolicy(sizePolicy9)

        self.gridLayout_7.addWidget(self.all_respondents_btn, 0, 0, 1, 1)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy10)

        self.gridLayout_7.addWidget(self.widget, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_7, 0, 0, 1, 2)

        self.tabWidget.addTab(self.widget_2, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_2), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0441\u043f\u043e\u043d\u0434\u0435\u043d\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

