# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(279, 424)
        Form.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 162, 105);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.title_edit = QtWidgets.QLineEdit(Form)
        self.title_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.title_edit.setPlaceholderText("")
        self.title_edit.setObjectName("title_edit")
        self.verticalLayout.addWidget(self.title_edit)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cost_hour_edit = QtWidgets.QLineEdit(Form)
        self.cost_hour_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cost_hour_edit.setPlaceholderText("")
        self.cost_hour_edit.setObjectName("cost_hour_edit")
        self.verticalLayout.addWidget(self.cost_hour_edit)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.full_cost_edit = QtWidgets.QLineEdit(Form)
        self.full_cost_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.full_cost_edit.setText("")
        self.full_cost_edit.setObjectName("full_cost_edit")
        self.verticalLayout.addWidget(self.full_cost_edit)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choice_img_btn = QtWidgets.QPushButton(Form)
        self.choice_img_btn.setObjectName("choice_img_btn")
        self.horizontalLayout.addWidget(self.choice_img_btn)
        self.imgname_edit = QtWidgets.QLineEdit(Form)
        self.imgname_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.imgname_edit.setObjectName("imgname_edit")
        self.horizontalLayout.addWidget(self.imgname_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.description_edit = QtWidgets.QTextEdit(Form)
        self.description_edit.setMinimumSize(QtCore.QSize(261, 70))
        self.description_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.description_edit.setPlaceholderText("")
        self.description_edit.setObjectName("description_edit")
        self.verticalLayout.addWidget(self.description_edit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.count_box = QtWidgets.QSpinBox(Form)
        self.count_box.setMaximum(100)
        self.count_box.setObjectName("count_box")
        self.horizontalLayout_2.addWidget(self.count_box)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.type_box = QtWidgets.QComboBox(Form)
        self.type_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.type_box.setObjectName("type_box")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.verticalLayout.addWidget(self.type_box)
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout.addWidget(self.add_btn)

        self.retranslateUi(Form)
        self.type_box.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить товар"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "Стоимость, руб. за час"))
        self.label_6.setText(_translate("Form", "Полная стоимость"))
        self.label_5.setText(_translate("Form", "Изображение"))
        self.choice_img_btn.setText(_translate("Form", "Выбрать"))
        self.label_4.setText(_translate("Form", "Описание"))
        self.description_edit.setDocumentTitle(_translate("Form", "Описание"))
        self.label_3.setText(_translate("Form", "Остаток:"))
        self.count_box.setSuffix(_translate("Form", " шт."))
        self.type_box.setPlaceholderText(_translate("Form", "Категория:"))
        self.type_box.setItemText(0, _translate("Form", "Стратегические"))
        self.type_box.setItemText(1, _translate("Form", "Вечериночные"))
        self.type_box.setItemText(2, _translate("Form", "Карточные"))
        self.type_box.setItemText(3, _translate("Form", "Абстрактные"))
        self.add_btn.setText(_translate("Form", "Добавить"))
