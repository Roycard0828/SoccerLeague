# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mensaje_error_borrarEquipo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Delete_Message(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 146)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 441, 41))
        self.label.setStyleSheet("color:black;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 100, 88, 34))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(120, 208, 9);\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:white;\n"
"    border-color:black;\n"
"    color:black;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">¡Debes seleccionar la celda que contiene el ID!</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
