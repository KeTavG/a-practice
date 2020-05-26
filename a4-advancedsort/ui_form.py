# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(648, 162)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.inputArray = QLineEdit(Form)
        self.inputArray.setObjectName(u"inputArray")

        self.verticalLayout.addWidget(self.inputArray)

        self.sortButton = QPushButton(Form)
        self.sortButton.setObjectName(u"sortButton")

        self.verticalLayout.addWidget(self.sortButton)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.sortedArrayCocktail = QLabel(Form)
        self.sortedArrayCocktail.setObjectName(u"sortedArrayCocktail")

        self.verticalLayout.addWidget(self.sortedArrayCocktail)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.sortedArrayQuick = QLabel(Form)
        self.sortedArrayQuick.setObjectName(u"sortedArrayQuick")

        self.verticalLayout.addWidget(self.sortedArrayQuick)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Advanced Sort", None))
        self.label.setText(QCoreApplication.translate("Form", u"Original array:", None))
        self.inputArray.setPlaceholderText(QCoreApplication.translate("Form", u"1 2 3", None))
        self.sortButton.setText(QCoreApplication.translate("Form", u"Sort", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Sorted array (cocktail sort):", None))
        self.sortedArrayCocktail.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Sorted array (quick sort):", None))
        self.sortedArrayQuick.setText("")
    # retranslateUi

