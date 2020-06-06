# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sr-tracker.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        MainWindow.setFont(font)

        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")

        # Tank
        self.t_layout = QtWidgets.QHBoxLayout()
        self.t_layout.setObjectName("t_layout")
        self.t_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.t_icon.setObjectName("t_icon")
        self.t_layout.addWidget(self.t_icon)
        self.t_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.t_number.setObjectName("t_number")
        self.t_layout.addWidget(self.t_number)
        self.t_right = QtWidgets.QVBoxLayout()
        self.t_right.setObjectName("t_right")
        self.t_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.t_edit.setObjectName("t_edit")
        self.t_right.addWidget(self.t_edit)
        self.t_update = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.t_update.setObjectName("t_update")
        self.t_right.addWidget(self.t_update)
        self.t_layout.addLayout(self.t_right)
        self.main_layout.addLayout(self.t_layout)

        self.line_1 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.main_layout.addWidget(self.line_1)

        # Damage
        self.d_layout = QtWidgets.QHBoxLayout()
        self.d_layout.setObjectName("d_layout")
        self.d_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.d_icon.setObjectName("d_icon")
        self.d_layout.addWidget(self.d_icon)
        self.d_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.d_number.setObjectName("d_number")
        self.d_layout.addWidget(self.d_number)
        self.d_right = QtWidgets.QVBoxLayout()
        self.d_right.setObjectName("d_right")
        self.d_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.d_edit.setObjectName("d_edit")
        self.d_right.addWidget(self.d_edit)
        self.d_update = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.d_update.setObjectName("d_update")
        self.d_right.addWidget(self.d_update)
        self.d_layout.addLayout(self.d_right)
        self.main_layout.addLayout(self.d_layout)

        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.main_layout.addWidget(self.line_2)

        # Support
        self.s_layout = QtWidgets.QHBoxLayout()
        self.s_layout.setObjectName("s_layout")
        self.s_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.s_icon.setObjectName("s_icon")
        self.s_layout.addWidget(self.s_icon)
        self.s_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.s_number.setObjectName("s_number")
        self.s_layout.addWidget(self.s_number)
        self.s_right = QtWidgets.QVBoxLayout()
        self.s_right.setObjectName("s_right")
        self.s_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.s_edit.setObjectName("s_edit")
        self.s_right.addWidget(self.s_edit)
        self.s_update = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.s_update.setObjectName("s_update")
        self.s_right.addWidget(self.s_update)
        self.s_layout.addLayout(self.s_right)
        self.main_layout.addLayout(self.s_layout)

        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.main_layout.addWidget(self.line_3)

        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout.setObjectName("bottom_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_layout.addItem(spacerItem)
        self.show_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.show_button.setObjectName("show_button")
        self.bottom_layout.addWidget(self.show_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_layout.addItem(spacerItem1)
        self.delete_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.bottom_layout.addWidget(self.delete_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_layout.addItem(spacerItem2)
        self.main_layout.addLayout(self.bottom_layout)
        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.t_edit, self.t_update)
        MainWindow.setTabOrder(self.t_update, self.d_edit)
        MainWindow.setTabOrder(self.d_edit, self.d_update)
        MainWindow.setTabOrder(self.d_update, self.s_edit)
        MainWindow.setTabOrder(self.s_edit, self.s_update)
        MainWindow.setTabOrder(self.s_update, self.show_button)
        MainWindow.setTabOrder(self.show_button, self.delete_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SR TRACKER"))
        self.t_icon.setText(_translate("MainWindow", "img"))
        self.t_number.setText(_translate("MainWindow", "number"))
        self.t_update.setText(_translate("MainWindow", "Update"))
        self.d_icon.setText(_translate("MainWindow", "img"))
        self.d_number.setText(_translate("MainWindow", "number"))
        self.d_update.setText(_translate("MainWindow", "Update"))
        self.s_icon.setText(_translate("MainWindow", "img"))
        self.s_number.setText(_translate("MainWindow", "number"))
        self.s_update.setText(_translate("MainWindow", "Update"))
        self.show_button.setText(_translate("MainWindow", "Show graphs"))
        self.delete_button.setText(_translate("MainWindow", "Clear all"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
