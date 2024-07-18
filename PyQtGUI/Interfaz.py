# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appGUI_SimlsfVBU.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(610, 538)
        self.tabDiseno1 = QTabWidget(Dialog)
        self.tabDiseno1.setObjectName(u"tabDiseno1")
        self.tabDiseno1.setGeometry(QRect(0, 0, 621, 541))
        font = QFont()
        font.setFamilies([u"Vensim Sans Arabic"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.tabDiseno1.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 451, 41))
        font1 = QFont()
        font1.setFamilies([u"Vensim Sans ExtraBold"])
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 450, 481, 31))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 141, 16))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 100, 91, 16))
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 100, 113, 21))
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(390, 100, 101, 21))
        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 60, 161, 31))
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 70, 141, 16))
        self.tabDiseno1.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableWidget = QTableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 20, 501, 431))
        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(70, 460, 481, 31))
        self.tabDiseno1.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 70, 221, 24))
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 70, 261, 24))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 111, 16))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 30, 161, 16))
        self.tabDiseno1.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabDiseno1.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabDiseno1.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabDiseno1.addTab(self.tab_6, "")

        self.retranslateUi(Dialog)

        self.tabDiseno1.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"DISENA TU COHETE", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cargar datos", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Diametro externo [mm]", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Espesor [mm]", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Nombre de tu vehiculo", None))
        self.tabDiseno1.setTabText(self.tabDiseno1.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Diseno", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Componente", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Tipo", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Longitud [m]", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Masa [kg]", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Posicion [m]", None));
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Cargar datos", None))
        self.tabDiseno1.setTabText(self.tabDiseno1.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Componentes", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Importar curva de empuje .csv", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Importar curva de variacion de masa .csv", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"EMPUJE", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"VARIACION DE MASA", None))
        self.tabDiseno1.setTabText(self.tabDiseno1.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Empuje y Masa", None))
        self.tabDiseno1.setTabText(self.tabDiseno1.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Atmosfera", None))
        self.tabDiseno1.setTabText(self.tabDiseno1.indexOf(self.tab_5), QCoreApplication.translate("Dialog", u"Lanzamiento", None))
        self.tabDiseno1.setTabText(self.tabDiseno1.indexOf(self.tab_6), QCoreApplication.translate("Dialog", u"Resultados", None))
    # retranslateUi

